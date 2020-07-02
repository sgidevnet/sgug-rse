%{?python_enable_dependency_generator}
%global pypi_name python-json-logger

# Missing license file and tests
# https://github.com/madzak/python-json-logger/issues/50

Name:           python-json-logger
Version:        0.1.7
Release:        13%{?dist}
Summary:        A python library adding a json log formatter

License:        BSD
URL:            http://github.com/madzak/python-json-logger
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
A python library adding a json log formatter

%package -n     python3-json-logger
Summary:        A python library adding a json log formatter
%{?python_provide:%python_provide python3-json-logger}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-json-logger
A python library adding a json log formatter


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


#%check
#%{__python3} setup.py test


%files -n python3-json-logger
%{python3_sitelib}/pythonjsonlogger
%{python3_sitelib}/python_json_logger-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-7
- Enable python dependency generator

* Wed Jan 02 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-6
- Subpackage python2-json-logger has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.7-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Jun 12 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.7-1
- Initial package.
