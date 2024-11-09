{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # Specify the Python version you want (e.g., python39, python310)
  buildInputs = [
    pkgs.python312         # Python version (use any version you need)
    pkgs.python312Packages.flask  # Flask package
  ];

  # Set environment variables if needed
  shellHook = ''
    echo "Nix shell with Flask is ready!"
  '';
}