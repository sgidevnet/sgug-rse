Summary: A utility which maintains a system''s symbolic links
Name: symlinks
URL: http://ibiblio.org/pub/Linux/utils/file/
Version: 1.7
Release: 1%{?dist}
License: Copyright only
# Upstream maintainer provided tarball, ibiblio no longer allowing uploads
Source0: http://ibiblio.org/pub/Linux/utils/file/%{name}-%{version}.tar.gz
# Taken from http://packages.debian.org/changelogs/pool/main/s/symlinks/symlinks_1.2-4.2/symlinks.copyright
Source1: symlinks-LICENSE.txt
BuildRequires: gcc

Patch100: symlinks.sgifixes.patch

%description
The symlinks utility performs maintenance on symbolic links.  Symlinks
checks for symlink problems, including dangling symlinks which point
to nonexistent files.  Symlinks can also automatically convert
absolute symlinks to relative symlinks.

Install the symlinks package if you need a program for maintaining
symlinks on your system.

%prep
%setup -q
cp %{SOURCE1} .

%patch100 -p1

# Place to build patches
#exit 1

%build
export CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS) %{build_ldflags}"
make CFLAGS="$CFLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 symlinks $RPM_BUILD_ROOT%{_bindir}
install -m 644 symlinks.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc symlinks-LICENSE.txt
%{_bindir}/symlinks
%{_mandir}/man1/symlinks.1*

%changelog
* Sat Jun 13 2020 Daniel Hams <daniel.hams@gmail.com> - 1.7-1
- Import into wip

* Wed Jan  8 2020 Tim Waugh <twaugh@redhta.com> - 1.7-1
- 1.7, fixes #1786376.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tim Waugh <twaugh@redhat.com> - 1.4-21
- Build requires gcc (bug #1606459).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Than Ngo <than@redhat.com> - 1.4-19
- fixed upstream URL reference
