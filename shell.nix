# shell.nix
with import <nixpkgs> {};

mkShell {
  # Base package environment
  buildInputs = [
    (nmap.overrideAttrs (old: {
      # Custom source files to be added to the Nmap share folder
      postInstall = ''
        mkdir -p $out/share/nmap/vulscan
        cp -r ./vulscan/* $out/share/nmap/vulscan
      '';
    }))
  ];
}
