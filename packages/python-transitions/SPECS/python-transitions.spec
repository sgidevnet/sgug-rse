%global srcname transitions

Name:           python-%{srcname}
Version:        0.7.2
Release:        2%{?dist}
Summary:        Object-oriented finite state machine implementation in Python

License:        MIT
URL:            https://github.com/pytransitions/transitions
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
A lightweight, object-oriented state machine implementation in Python.

%package -n python3-%{srcname}
Summary: %{summary}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-six
BuildRequires: python3-dill
BuildRequires: python3-graphviz
BuildRequires: python3-pygraphviz
BuildRequires: python3-pytest
BuildRequires: python3-pycodestyle
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A lightweight, object-oriented state machine implementation in Python.

%package docs
Summary:        Documentation for %{name}

%description docs
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
pytest-%{python3_version} -v --doctest-modules

%files -n python3-%{srcname}
%license LICENSE
%doc Changelog.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/*.egg-info/

%files docs
%license LICENSE
%doc examples Changelog.md README.md

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.9

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-1
- Clean-up spec file
- Update to latest upstream release 0.7.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1 (#1751968).
- https://github.com/pytransitions/transitions/blob/0.7.1/Changelog.md

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0 (#1743448).
- https://github.com/pytransitions/transitions/blob/0.7.0/Changelog.md

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.9-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.9-2
- Enable python dependency generator

* Thu Dec 20 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.9-1
- Update to 0.6.9.
- https://github.com/pytransitions/transitions/blob/0.6.9/Changelog.md

* Fri Dec 07 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.8-1
- Drop Python 2 subpackage.

* Tue Jul 31 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.8-1
- Update to 0.6.8.
- Add more BuildRequires.
- Split docs into their own subpackage.

* Thu Apr 12 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.4-1
- Initial release.
