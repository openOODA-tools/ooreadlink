Name:           ooreadlink
Version:        0.1.0
Release:        1%{?dist}
Summary:        Resolves symbolic link targets and canonicalizes path sequences without traversal.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooreadlink
Source0:        ooreadlink-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooreadlink is a sovereign, capability-bounded SYMLINK RESOLVER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooreadlink
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooreadlink-uninstall

%files
/usr/bin/ooreadlink
/usr/bin/ooreadlink-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
