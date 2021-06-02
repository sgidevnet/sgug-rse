Name:           bibutils
Version:        6.7
Release:        3%{?dist}
Summary:        Bibliography conversion tools

License:        GPLv2
URL:            http://sourceforge.net/p/bibutils/home/Bibutils/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{version}_src.tgz

BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc

%description
The bibutils package converts between various bibliography
formats using a common MODS-format XML intermediate.


%package libs
Summary:        Bibutils library
License:        GPL+

%description libs
Bibutils library.


%package devel
Summary:        Development files for bibutils
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
License:        GPL+

%description devel
Bibutils development files.


%prep
%autosetup -n %{name}_%{version}


%build
./configure \
    --install-dir %{buildroot}%{_bindir} \
    --install-lib %{buildroot}%{_libdir} \
    --dynamic
make DISTRO_CFLAGS="%optflags" LDFLAGSIN="%{?__global_ldflags}"

xsltproc -o bibutils.1 --nonet %{_datadir}/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl bibutils.dbk


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir}
%make_install

mkdir -p %{buildroot}%{_includedir}/%{name}
cp -p lib/*.h %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_libdir}/pkgconfig 
cp -p lib/%{name}.pc %{buildroot}%{_libdir}/pkgconfig
sed -i -e 's!\\!!g' -e 's!libdir=${prefix}/lib!libdir=%{_libdir}!' -e 's!${includedir}!${includedir}/%{name}!' %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{name}.1 %{buildroot}%{_mandir}/man1

for i in $(cd %{buildroot}%{_bindir}; ls *); do
  ln -s bibutils.1 %{buildroot}%{_mandir}/man1/$i.1
done


%files
%doc ChangeLog
%{_bindir}/*
%{_mandir}/man1/*.1*


%files libs
%license Copying
%{_libdir}/libbibutils.so.*


%files devel
%{_includedir}/%{name}
%{_libdir}/libbibutils.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 05 2018 Vasiliy N. Glazov <vascom2@gmail.com> 6.7-1
- Update to 6.7

* Mon Jul 23 2018 Vasiliy N. Glazov <vascom2@gmail.com> 6.6-1
- Update to 6.6
- Drop patch
- Clean spec

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jens Petersen <petersen@redhat.com> - 6.5-1
- update to version 6.5
- build with LDFLAGS (#1541039)

* Wed Jun  6 2018 Jens Petersen <petersen@redhat.com> - 6.3-1
- update to 6.3 which addresses CVE-2018-10773 CVE-2018-10774 CVE-2018-10775
  (#1577259)

* Mon Feb 19 2018 Jens Petersen <petersen@redhat.com> - 6.2-4
- BR gcc

* Wed Feb 14 2018 Jens Petersen <petersen@redhat.com> - 6.2-3
- fix the build with CFLAGS and LDFLAGS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Jens Petersen <petersen@redhat.com> - 6.2-2
- using distro LDFLAGS (#1541039)

* Sat Jan 13 2018 Jens Petersen <petersen@redhat.com> - 6.2-1
- update to 6.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 5.5-1
- update to 5.5

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun  5 2013 Jens Petersen <petersen@redhat.com> - 5.0-1
- update to 5.0

* Mon Jan 28 2013 Jens Petersen <petersen@redhat.com> - 4.17-1
- update to 4.17
- patch and use upstream's Makefile

* Thu Jan 10 2013 Jens Petersen <petersen@redhat.com> - 4.16-1
- update to 4.16
- update License to only GPLv2
- no longer needs csh to build

* Thu Oct  4 2012 Jens Petersen <petersen@redhat.com> - 4.15-4
- tcsh provides csh so no need to patch configure for tcsh
- change license to GPL+ for the code and GPLv2 for the manpage

* Tue Oct  2 2012 Jens Petersen <petersen@redhat.com> - 4.15-3
- improve summary and description (#861922)
- build and install docbook manpage which is GPLv2+ (#861922)
- use _isa (#861922)

* Tue Oct  2 2012 Jens Petersen <petersen@redhat.com> - 4.15-2
- BR tcsh

* Mon Oct  1 2012 Jens Petersen <petersen@redhat.com> - 4.15-1
- initial packaging
