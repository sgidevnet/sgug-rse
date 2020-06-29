%global srcname notario

Name:           python-notario
Version:        0.0.16
Release:        8%{?dist}
Summary:        A dictionary validator
License:        MIT
URL:            https://github.com/alfredodeza/notario
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
Notario is flexible and succinct Python dictionary validator with the ability
to validate against both keys and values. Schemas are smaller and readable
representations of data being validated.

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3

%description -n python3-%{srcname}
Notario is flexible and succinct Python dictionary validator with the ability
to validate against both keys and values. Schemas are smaller and readable
representations of data being validated.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{py3_build}

%install
%py3_install

%check
py.test-%{python3_version} -v notario/tests

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.16-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.16-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.16-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Ken Dreyer <kdreyer@redhat.com> - 0.0.16-3
- Use %%pypi_source macro

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Ken Dreyer <kdreyer@redhat.com> - 0.0.16-1
- Update to 0.0.16

* Sat Jan 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.14-4
- Subpackage python2-notario has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.14-2
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Ken Dreyer <ktdreyer@ktdreyer.com> 0.0.14-1
- Update to 0.0.14 (rhbz#1592603)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.13-2
- Rebuilt for Python 3.7

* Thu May 17 2018 Ken Dreyer <ktdreyer@ktdreyer.com> 0.0.13-1
- Update to 0.0.13 (rhbz#1574272)
- Build py3 on RHEL beyond 7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Ken Dreyer <ktdreyer@ktdreyer.com> 0.0.12-1
- Update to 0.0.12
- New Source0 URL format

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.11-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 02 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.11-2
- Use %%global macro instead of %%define (rhbz#1305154)

* Tue Mar 01 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.11-1
- Update to latest upstream release
- Drop older python macros.

* Mon Feb 15 2016 Ken Dreyer <kdreyer@redhat.com> - 0.0.9-1
- Update to latest upstream release

* Mon Feb 15 2016 Ken Dreyer <kdreyer@redhat.com> - 0.0.8-2
- Fall back to older python macros. The newer python macros are only
  available in EPEL 7, not RHEL 7 (see rhbz#1306861). Add fallbacks so
  we can still build and install on RHEL 7.
- Use HTTPS upstream URLs.

* Fri Feb 05 2016 Ken Dreyer <kdreyer@redhat.com> 0.0.8-1
- Initial package
