Name:           nim-srpm-macros
Version:        3
Release:        1%{?dist}
Summary:        RPM macros for building Nimble source packages

License:        MIT
URL:            https://pagure.io/nim2rpm
Source0:        https://releases.pagure.org/nim2rpm/nim2rpm-%{version}.tar.xz

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n nim2rpm-%{version}

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmconfigdir}/macros.d data/macros.nim-srpm

%files
%license LICENSE
%{_rpmconfigdir}/macros.d/macros.nim-srpm

%changelog
* Mon Dec 09 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 3-1
- Update to v3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2-1
- Update to v2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 12 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 1-1
- Initial package
