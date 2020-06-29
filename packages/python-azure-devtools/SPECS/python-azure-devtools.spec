%{?python_enable_dependency_generator}

%global srcname azure-devtools
%global common_description This package contains tools to aid in developing Python-based Azure code.

Name:           python-%{srcname}
Version:        1.0.0
Release:        10%{?dist}
Summary:        Devtools for Azure SDK and CLI for Python

License:        MIT
URL:            https://github.com/Azure/azure-python-devtools
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Needed for tests
BuildRequires:  python3-configargparse
BuildRequires:  python3-six
BuildRequires:  python3-vcrpy
BuildArch:      noarch

%description
%{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}


%prep
%autosetup -n azure-python-devtools-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m unittest discover -s src/


%files -n python3-%{srcname}
%doc README.rst doc/
%license LICENSE
%{python3_sitelib}/azure_devtools/
%{python3_sitelib}/azure_devtools-*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.0-5
- Enable Python generators
- Enable tests
- Spec cleanup

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.0-3
- Fix dependency on python-vcrpy for Fedora <= 27

* Tue Nov 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.0-2
- Don't glob everything under the Python sitelib directory

* Sat Nov 03 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.0-1
- Initial RPM release
