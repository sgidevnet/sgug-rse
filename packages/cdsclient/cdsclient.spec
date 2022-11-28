Name:           cdsclient
Version:        3.84
Release:        8%{?dist}
Summary:        Tools to query databases at CDS

License:        GPLv3
URL:            http://cdsarc.u-strasbg.fr/doc/cdsclient.html
Source0:        ftp://cdsarc.u-strasbg.fr/pub/sw/%{name}-%{version}.tar.gz
# Patch to get useful debuginfo. strip was called in Makefile before and compiler
# flags were ignored, submitted upstream by email
Patch0:         fix_makefile_debuginfo.patch
# Upstream places abibcode.awk in /usr/bin although it is not an executable but
# arch independent data
Patch1:         abibcode_share_location_trim.patch

BuildRequires:  gcc

# wget is used by some of the shell scripts to fetch data from servers
Requires:       wget

%description
The cdsclient package is a set of C and shell routines which can be built on
Unix stations or PCs running Linux, which once compiled allow to query some 
databases located at CDS or on mirrors over the network.

The cdsclient package includes two generic query programs:
- vizquery, a program to remotely query VizieR. It connects the VizieR server
  via the HTTP protocol (requires an access to the port 80)
- find_cats, a program for fast access to large surveys from a list of 
  positions, via a dedicated client (requires an access to the port 1660)
  Specific programs like find2mass or finducac3 are connecting directly to one
  of the very large surveys available from CDS (a very large survey has 107 
  or more rows).
  

%prep
%setup -q
%patch0 -p1
%patch1 -p1


%build
%configure 
make %{?_smp_mflags}


%install
# make install doesn't create directories
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_datadir}/%{name}
%make_install PREFIX=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}
# Remove this unneeded stuff
rm -f %{buildroot}%{_prefix}/versions
rm -f %{buildroot}%{_bindir}/find_cats.gz
# Move abibcode.awk (non executable called by abibcode) to /usr/share/cdsclient/
mv %{buildroot}%{_bindir}/abibcode.awk %{buildroot}%{_datadir}/%{name}/abibcode.awk
%{_fixperms} %{buildroot}/*


%files
%if 0%{?fedora} >= 21
%license COPYING COPYRIGHT
%else
%doc COPYING COPYRIGHT
%endif
%dir %{_datadir}/%{name}
%dir %{_mandir}/mantex
%{_bindir}/*
%{_datadir}/%{name}/abibcode.awk
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/mantex/*


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.84-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.84-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Christian Dersch <lupinix.fedora@gmail.com> - 3.84-6
- BuildRequires: gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.84-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.84-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Christian Dersch <lupinix@mailbox.org> - 3.84-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 04 2016 Christian Dersch <lupinix@mailbox.org> - 3.83-1
- new version

* Sat Feb 06 2016 Christian Dersch <lupinix@fedoraproject.org> - 3.81-1
- new version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Christian Dersch <lupinix@fedoraproject.org> - 3.80-1
- new upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr  3 2015 Christian Dersch <lupinix@fedoraproject.org> - 3.79-1
- new upstream release

* Sun Jan 25 2015 Christian Dersch <lupinix@fedoraproject.org> - 3.78-3
- spec cleanups

* Sun Jan 25 2015 Christian Dersch <lupinix@fedoraproject.org> - 3.78-2
- move non-executable file abibcode.awk to /usr/share/cdsclient

* Mon Jan 19 2015 Christian Dersch <lupinix@fedoraproject.org> - 3.78-1
- new upstream release
- patch Makefile to be able to generate useful debuginfo
- enable debuginfo

* Mon Jan 12 2015 Christian Dersch <lupinix@fedoraproject.org> - 3.77-1
- initial spec
