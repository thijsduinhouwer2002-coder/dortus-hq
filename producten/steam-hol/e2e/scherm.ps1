# Maakt een schermafbeelding van het hele bureaublad (Windows-runner). Gebruik: scherm.ps1 <uitbestand.png>
param([string]$uit)
Add-Type -AssemblyName System.Windows.Forms, System.Drawing
$b = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bmp = New-Object System.Drawing.Bitmap $b.Width, $b.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen($b.Location, [System.Drawing.Point]::Empty, $b.Size)
$bmp.Save($uit, [System.Drawing.Imaging.ImageFormat]::Png)
# Bewijs in het log: kleur midden in de lucht boven de strook (moet het venster eronder zijn) en in de strook.
$lucht = $bmp.GetPixel([int]($b.Width/2), $b.Height - 48 - 200)
$strook = $bmp.GetPixel([int]($b.Width/2), $b.Height - 48 - 30)
Write-Output "SCHERM $uit $($b.Width)x$($b.Height) lucht=$lucht strook=$strook"
