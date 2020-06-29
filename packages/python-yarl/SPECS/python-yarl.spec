%global srcname yarl

Name:           python-%{srcname}
Version:        1.4.2
Release:        3%{?dist}
Summary:        A Python module to handle URLs

License:        ASL 2.0
URL:            https://yarl.readthedocs.io
Source0:        https://github.com/aio-libs/yarl/releases/download/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc

%description
The module provides handy URL class for URL parsing and changing.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-multidict
BuildRequires:  python3-idna
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
The module provides handy URL class for URL parsing and changing.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc CHANGES.rst README.rst
%license LICENSE
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*.egg-info/

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.2-1
- Update to latest upstream release 1.4.2 (rhbz#1758088)

* Thu Dec 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update to latest upstream release 1.4.1 (rhbz#1758088)

* Mon Dec 02 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to latest upstream release 1.4.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-3
- Remove dep generator

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-2
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.6-1
- Update to latest upstream release 1.2.6 (rhbz#1588495)

* Thu May 24 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.5-1
- Update to latest upstream release 1.2.5 (rhbz#1582015)

* Tue May 08 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.4-1
- Update to latest upstream release 1.2.4 (rhbz#1575970)

* Mon May 07 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.3-1
- Update to latest upstream release 1.2.3 (rhbz#1574065)

* Sat May 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to latest upstream release 1.2.2 (rhbz#1574065)

* Fri May 04 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Update to latest upstream release 1.2.1 (rhbz#1574065)

* Mon Feb 19 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to latest upstream release 1.1.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Fri Jan 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-2
- Enable usage of dependency generator

* Mon Jan 15 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to latest upstream release 1.0.0

* Thu Jan 11 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.18.0-1
- Update to latest upstream release 0.18.0

* Sun Dec 31 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.17.0-1
- Update to latest upstream release 0.17.0 (rhbz#1523436)

* Fri Dec 08 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.0-1
- Update to latest upstream release 0.16.0 (rhbz#1523436)

* Fri Nov 24 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.15.0-1
- Update to latest upstream release 0.15.0

* Tue Nov 14 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.2-1
- Update to latest upstream release 0.14.2

* Tue Nov 14 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.1-1
- Update to latest upstream release 0.14.1

* Sat Nov 11 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-1
- Update to latest upstream release 0.14.0 (rhbz#1512195)

* Sun Oct 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.0-2
- Fixes and cleanups in spec file

* Sun Oct 01 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.0-1
- Update to latest upstream release 0.13.0 (rhbz#1497531)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Update to latest upstream release 0.12.0 (rhbz#1471102)

* Wed Jun 28 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-1
- Update to latest upstream release 0.11.0 (rhbz#1465202)

* Wed Jun 14 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.3-1
- Update to 0.10.3 (rhbz#1461225)

* Tue May 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Wed Mar 15 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.0-1
- Update to latest upstream release 0.10.0 (rhbz#1432279)

* Mon Feb 20 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.8-1
- Update to latest upstream release 0.9.8 (rhbz#1423061)

* Thu Feb 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.6-1
- Update to 0.9.6

* Thu Feb 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-1
- Update to 0.9.2

* Wed Feb 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.8.1-4
- Fix BRs

* Tue Feb 07 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-3
- Update BR

* Fri Jan 27 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-2
- Don't remove _quoting.c

* Sat Jan 21 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-1
- Update to latest upstream release 0.8.1
- Remove _quoting.c

* Mon Nov 21 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-2
- Update Source0, summary

* Fri Nov 18 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Initial package
