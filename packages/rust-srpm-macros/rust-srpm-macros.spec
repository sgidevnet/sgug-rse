Name:           rust-srpm-macros
Version:        10
Release:        2%{?dist}
Summary:        RPM macros for building Rust source packages

License:        MIT
URL:            https://pagure.io/fedora-rust/rust2rpm
Source:         https://releases.pagure.org/fedora-rust/rust2rpm/rust2rpm-%{version}.tar.xz

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n rust2rpm-%{version} -p1
# https://pagure.io/koji/issue/659
sed -i -e 's/i686/%%{ix86}/' data/macros.rust-srpm

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} data/macros.rust-srpm

%files
%license LICENSE
%{_rpmmacrodir}/macros.rust-srpm

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10-1
- Update to 10

* Sat Jun 08 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 9-3
- Implement %%__cargo_skip_build

* Sat Jun 08 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 9-2
- Use %%ix86 as workaround

* Sun May 05 09:14:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 9-1
- Update to 9

* Tue Apr 23 21:17:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8-1
- Update to 8

* Tue Apr 23 16:16:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7-1
- Update to 7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6-3
- Add %%version_no_tilde

* Sat Jan 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6-2
- Add support for %%crates_source

* Sun Sep 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6-1
- Update to 6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5-1
- Update to 5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4-2
- Include license

* Fri Jul 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4-1
- Update to 4

* Tue Jun 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3-1
- Initial package
