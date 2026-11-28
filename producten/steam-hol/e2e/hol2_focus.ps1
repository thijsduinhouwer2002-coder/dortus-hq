# Olaf, 28 nov 2026 (issue #401, Daan #394 moet 2 en 3). Windows-runner: krijgt de besturen-stand van Hol 2.0 echte
# toetsen, en gaat de focus daarna terug naar Kladblok?
#   1. Kladblok vooraan (klik erin), dan HetHol.exe met toetsproef=1 (Gloop staat stil tot de besturen-stand).
#   2. Echte muisklik op Gloop, echte toets D 1,2 s, dan Esc.  Moet: "besturen aan", Gloop x anders, "focus terug naar".
#   3. Na Esc een echte letter q typen: die moet in Kladblok staan, niet in het hol.
#   4. Nog een klik op Gloop en 12 s niets: "10 s geen toets" en Kladblok weer vooraan.
# Gebruik: hol2_focus.ps1 <exe> <uitmap>   Schrijft <uitmap>/focus.txt en focus.log; exit 1 bij een FOUT.
param([string]$exe, [string]$uit)
Add-Type -AssemblyName System.Windows.Forms
Add-Type @"
using System; using System.Text; using System.Runtime.InteropServices;
public class W {
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern void keybd_event(byte vk, byte scan, uint f, IntPtr e);
  [DllImport("user32.dll")] public static extern uint MapVirtualKey(uint code, uint type);
  [DllImport("user32.dll")] public static extern IntPtr FindWindowEx(IntPtr p, IntPtr a, string klas, string titel);
  [DllImport("user32.dll", CharSet = CharSet.Unicode)] public static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, StringBuilder l);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  public struct RECT { public int L, T, R, B; }
  public static uint Pid(IntPtr h) { uint p; GetWindowThreadProcessId(h, out p); return p; }
  public static string Tekst(IntPtr h) { var sb = new StringBuilder(4096); SendMessage(h, 0x000D, (IntPtr)4096, sb); return sb.ToString(); }
}
"@
$klik = Join-Path $PSScriptRoot "klik.ps1"
$fout = 0; $r = @()
function Voor { $p = [W]::Pid([W]::GetForegroundWindow()); try { (Get-Process -Id $p).ProcessName } catch { "?" } }
# met scancode, zoals een echt toetsenbord (het hol leest de plek van de toets)
function Toets([byte]$vk, [int]$ms) { $sc = [byte][W]::MapVirtualKey($vk, 0); [W]::keybd_event($vk, $sc, 0, [IntPtr]::Zero); Start-Sleep -Milliseconds $ms; [W]::keybd_event($vk, $sc, 2, [IntPtr]::Zero) }
function Log { Get-Content "$uit/focus.log" -ErrorAction SilentlyContinue | Out-String }

# 1. Kladblok vooraan
$np = Start-Process notepad.exe -PassThru; Start-Sleep 3
$np.Refresh(); $rc = New-Object W+RECT; [W]::GetWindowRect($np.MainWindowHandle, [ref]$rc) | Out-Null
& $klik ([int](($rc.L + $rc.R) / 2)) ([int](($rc.T + $rc.B) / 2)) | Out-Null; Start-Sleep 1
$r += "voor de start vooraan: $(Voor)"
Remove-Item "$uit/focus.log" -ErrorAction SilentlyContinue
$p = Start-Process -FilePath $exe -ArgumentList "-- toetsproef=1 zaad=7 duur=70 log=$uit/focus.log" -PassThru
Start-Sleep 8
$r += "na de start van het hol vooraan: $(Voor) (moet notepad blijven)"
$m = [regex]::Match((Log), "gloop venster x=(-?\d+) y=(-?\d+)")
$wa = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
$s = [regex]::Match((Log), "venster=\((\d+), (\d+)\)")
$vh = [int]$s.Groups[2].Value
$gx = $wa.X + [int]$m.Groups[1].Value; $gy = $wa.Bottom - $vh + [int]$m.Groups[2].Value
$r += "Gloop op het scherm: $gx,$gy (venster $vh hoog, werkvlak $($wa.Width)x$($wa.Height))"

# 2. klik op Gloop, D, Esc
& $klik $gx $gy | Out-Null; Start-Sleep 1
$r += "na de klik op Gloop vooraan: $(Voor)"
Toets 0x44 1200; Start-Sleep -Milliseconds 600
Toets 0x1B 80; Start-Sleep 1
$l = Log
$aan = [regex]::Match($l, "besturen aan \(klik op Gloop\) gloop x=(\d+)")
$esc = [regex]::Match($l, "besturen uit \(Esc\) gloop x=(\d+)[^\r\n]*")
if (-not $aan.Success) { $r += "FOUT: geen 'besturen aan (klik op Gloop)'"; $fout++ }
elseif (-not $esc.Success) { $r += "FOUT: geen 'besturen uit (Esc)'"; $fout++ }
else {
  $dx = [int]$esc.Groups[1].Value - [int]$aan.Groups[1].Value
  $r += "D 1,2 s: Gloop x $($aan.Groups[1].Value) naar $($esc.Groups[1].Value) ($dx spelpx)"
  if ($dx -le 3) { $r += "FOUT: Gloop liep niet naar rechts met D"; $fout++ }
  $r += "log bij Esc: $($esc.Value)"
  if ($esc.Value -notmatch "focus terug naar") { $r += "FOUT: focus niet teruggezet"; $fout++ }
}

# 3. een letter na Esc moet in Kladblok staan
$r += "na Esc vooraan: $(Voor)"
Toets 0x51 60; Start-Sleep -Milliseconds 800
$np.Refresh()
$ed = [W]::FindWindowEx($np.MainWindowHandle, [IntPtr]::Zero, "Edit", $null)
if ($ed -eq [IntPtr]::Zero) { $ed = [W]::FindWindowEx($np.MainWindowHandle, [IntPtr]::Zero, "RichEditD2DPT", $null) }
$txt = if ($ed -ne [IntPtr]::Zero) { [W]::Tekst($ed) } else { "(geen tekstvak gevonden)" }
$r += "tekst in Kladblok na de letter q: '$txt'"
if ($txt -notmatch "q") { $r += "FOUT: de letter kwam niet in Kladblok"; $fout++ }

# 4. klik op Gloop en 12 s niets: terug na 10 s
& $klik $gx $gy | Out-Null; Start-Sleep 12
$l = Log
$tien = [regex]::Match($l, "besturen uit \(10 s geen toets\)[^\r\n]*")
$r += "na 12 s stil vooraan: $(Voor)"
if (-not $tien.Success) { $r += "FOUT: geen 'besturen uit (10 s geen toets)'"; $fout++ } else { $r += "log: $($tien.Value)"; if ($tien.Value -notmatch "focus terug naar") { $r += "FOUT: focus niet terug na 10 s"; $fout++ } }
if ((Voor) -ne "notepad") { $r += "FOUT: na 10 s staat Kladblok niet vooraan"; $fout++ }

Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
Stop-Process -Id $np.Id -Force -ErrorAction SilentlyContinue
$r += "focus en besturen: $fout FOUT"
$r | Set-Content "$uit/focus.txt"; $r | ForEach-Object { Write-Output $_ }
if ($fout -gt 0) { exit 1 }
