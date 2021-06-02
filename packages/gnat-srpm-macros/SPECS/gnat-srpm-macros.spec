Name:           gnat-srpm-macros
Version:        4
Release:        10%{?dist}
Summary:        RPM macros needed when source packages that need GNAT are built
Summary(sv):    RPM-makron som behövs när källkodspaket som behöver GNAT byggs

License:        MIT
URL:            https://src.fedoraproject.org/rpms/gnat-srpm-macros
Source1:        macros.gnat-srpm
BuildArch:      noarch


%description
This package contains RPM macros that need to be available when source RPM
packages that need the GNAT tools are built. It is a standalone package in
order to have as few dependencies as possible.

%description -l sv
Det här paketet innehåller RPM-makron som behöver finnas tillgängliga när käll-
RPM-paket som behöver GNAT-verktygen byggs. Det är ett fristående paket för att
bero av så få andra paket som möjligt.


%prep
# nothing to do


%build
# nothing to do


%install
mkdir -p %{buildroot}/%{rpmmacrodir}
install -p -m 0644 -t %{buildroot}/%{rpmmacrodir} %{SOURCE1}


%files
%{rpmmacrodir}/*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb  6 2019 Pavel Zhukov <pzhukov@redhat.com> - 4-9
- Add back ppc64le

* Tue Feb  5 2019 Pavel Zhukov <pzhukov@redhat.com> - 4-8
- Add back ix86 arch and temporary disable ppc64

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Pavel Zhukov <pzhukov@redhat.com> - 4-3
- Dropping i686 from the list of gprbuild arches due to 1444614

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 28 2016 Björn Persson <Bjorn@Rombobjörn.se> - 4-1
- GPRbuild is available on s390x and ppc64le.
- ia64, ppc and alpha are inactive.

* Tue Mar 22 2016 Björn Persson <Bjorn@Rombobjörn.se> - 3-1
- GNAT has been bootstrapped on s390x and ppc64le.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Björn Persson <bjorn@rombobjörn.se> - 2-1
- Added ARM to GPRbuild_arches, as GPRbuild now works on ARM.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Sep 14 2014 Björn Persson <bjorn@rombobjörn.se> - 1-1
- Separated GNAT_arches from redhat-rpm-config.
- Introduced GPRbuild_arches, excluding ARM.
- Added ppc64p7 to synchronize with the GCC package.
