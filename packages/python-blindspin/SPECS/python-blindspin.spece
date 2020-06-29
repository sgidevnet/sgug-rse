%global srcname blindspin

%global _description\
Spinner class to show a simple spinner where a progress bar is not a\
feasible option.

Name:           python-%{srcname}
Version:        2.0.1
Release:        10%{?dist}
Summary:        Braille Spinner for Click

License:        MIT
URL:            https://github.com/kennethreitz/blindspin
Source0:        https://github.com/kennethreitz/blindspin/archive/v%{version}/%{srcname}/%{srcname}-%{version}.tar.gz
#Source0:       https://files.pythonhosted.org/packages/source/b/%%{srcname}/%%{srcname}-%%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# tests deps, click spinner not available yet:
#BuildRequires:  python3dist(click)
#BuildRequires:  python3dist(click-spinner)
#BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(six)

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Fix bad version in GitHub Tarball
sed -i "s/version='0.1.0'/version='%{version}'/" setup.py

%build
%py3_build

%install
%py3_install

#check
#__python3 -m pytest -v

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.7

* Sat Jun 23 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Prepare for tests
- Remove unneeded runtime requirements

* Fri Jun 08 2018 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 2.0.1-1
- Initial package.
