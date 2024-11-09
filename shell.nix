# shell.nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell rec {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.requests
    pkgs.python3Packages.scapy
    pkgs.python3Packages.flask
  ];

  # Optional: set up a Python environment
  shellHook = ''
    echo "Welcome to the nix-shell with Python!"
  '';
}
