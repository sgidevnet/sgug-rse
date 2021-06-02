Name: module-macros
Version: 0.1
Release: 6%{?dist}
Summary: Macros for creating modules

License: MIT
Source0: macros.module

BuildArch: noarch

%description
This package provides macros for module development.

%prep

%build

%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{rpmmacrodir}

%files
%{rpmmacrodir}
%{rpmmacrodir}/macros.module

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 clime <clime@redhat.com> 0.1-1
- Initial version
