%global srcname pytest-helpers-namespace
%global srcname_ pytest_helpers_namespace

Name:           python-%{srcname}
Version:        2019.1.8
Release:        7%{?dist}
Summary:        PyTest Helpers Namespace

License:        ASL 2.0
URL:            https://github.com/saltstack/pytest-helpers-namespace
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Provides a helpers pytest namespace which can be used to register helper
functions without requiring you to import them on your actual tests to use
them.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%{?python_enable_dependency_generator}

%description -n python3-%{srcname}
Provides a helpers pytest namespace which can be used to register helper
functions without requiring you to import them on your actual tests to use
them.


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname_}
%{python3_sitelib}/%{srcname_}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.1.8-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.1.8-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.1.8-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2019.1.8-1
- Update to latest version

* Tue Aug 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2017.11.11-1
- Initial package.
