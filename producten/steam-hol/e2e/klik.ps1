# Klikt met de muis op schermpunt x,y (Windows-runner). Gebruik: klik.ps1 <x> <y>
param([int]$x, [int]$y)
Add-Type @"
using System; using System.Runtime.InteropServices;
public class Muis { [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
  [DllImport("user32.dll")] public static extern void mouse_event(uint f, uint dx, uint dy, uint d, IntPtr e); }
"@
[Muis]::SetCursorPos($x, $y) | Out-Null
Start-Sleep -Milliseconds 200
[Muis]::mouse_event(0x0002, 0, 0, 0, [IntPtr]::Zero); Start-Sleep -Milliseconds 80
[Muis]::mouse_event(0x0004, 0, 0, 0, [IntPtr]::Zero)
Write-Output "KLIK op $x,$y"
