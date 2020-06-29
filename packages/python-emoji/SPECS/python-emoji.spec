%global appname emoji

%global appsum Emoji library for Python
%global appdesc Full featured simple emoji library for Python

Name: python-%{appname}
Version: 0.5.4
Release: 4%{?dist}
Summary: %{appsum}

License: BSD
URL: https://pypi.python.org/pypi/%{appname}
Source0: %{pypi_source %{appname}}
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3dist(nose)
BuildRequires: python3dist(coverage)

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{appname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{appname}
%license LICENSE.txt
%doc README.rst CHANGES.md
%{python3_sitelib}/%{appname}
%{python3_sitelib}/%{appname}-*.egg-info

%changelog
* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.4-4
- Added python3-setuptools to build requirements.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.4-1
- Updated to version 0.5.4.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.3-1
- Updated to version 0.5.3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-1
- Initial SPEC release.
