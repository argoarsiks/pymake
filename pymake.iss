[Setup]
AppId={{78ac235d-a664-44dc-bea9-a7df53162dce}}
AppName=pymake
AppVersion=1.0.0
DefaultDirName={autopf}\pymake
DefaultGroupName=pymake
OutputDir=dist
OutputBaseFilename=pymake-setup-1.0.0
PrivilegesRequired=lowest
WizardStyle=modern

[Files]
Source: "dist\pymake.exe"; DestDir: "{app}"; Flags: ignoreversion

[Run]
Filename: "{app}\pymake.exe"; Flags: nowait runhidden