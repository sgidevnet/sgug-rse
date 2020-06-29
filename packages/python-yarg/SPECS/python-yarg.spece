%{?python_enable_dependency_generator}
%global srcname yarg

%global _description\
Yarg is an easy to use PyPI client built on top of Python's requests library.

Name:           python-%{srcname}
Version:        0.1.9
Release:        11%{?dist}
Summary:        An easy to use PyPI client

License:        MIT
URL:            https://yarg.readthedocs.org/
Source0:        https://github.com/kura/yarg/archive/%{version}/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(mock)

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE-REQUESTS LICENSE
%doc README.rst
# Ignore tests
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-5
- Enable python dependency generator

* Sun Jan 13 2019 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.1.9-4
- Fix Bug #1655700 - Exclude 'tests' folder

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.1.9-2
- Add additional build dependency for tests

* Sun Jun 24 2018 Dhanesh B. Sabane <dhanesh95@disroot.org> - 0.1.9-1
- Initial package.
