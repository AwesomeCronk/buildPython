For ($i = 0; $i -lt $args.Length; $i++)
{
    $current = $args[$i]
    Write-Output "Building $current.exe..."
    Remove-Item "$current.exe" -ErrorAction Ignore #Delete the original .exe if it exists
    pyinstaller --onefile "$current.py" #Build with PyInstaller
    Move-Item "dist/$current.exe" ./ #Move the .exe to the current directory
    Remove-Item -Recurse -Force dist #Delete the dist directory
    Remove-Item -Recurse -Force build #Recursively delete the contents of the build directory
    #Remove-Item build #Delete the build directory
    Remove-Item "$current.spec" #Delete the .spec file
    Write-Output "Done building $current.exe."
}
