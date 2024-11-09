{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python312   # Python 3.12
    pkgs.nmap
  ];

  shellHook = ''
    echo "Nix shell with Python 3.12, requests, and scapy is ready."
  '';
}