%global _description ISO 3166-1 defines two-letter, three-letter, and three-digit country\
codes. python-iso3166 is a self-contained module that converts between these\
codes and the corresponding country name.

%global srcname iso3166

Name:           python-%{srcname}
Version:        1.0.1
Release:        3%{?dist}
Summary:        Self-contained ISO 3166-1 country definitions

License:        MIT
URL:            https://github.com/deactivated/%{name}/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=$PWD py.test-%{python3_version}


%files -n python3-%{srcname}
%doc CHANGES README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1
- Add tests

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0-1
- Update to 1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-2
- Subpackage python2-iso3166 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Aug 05 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9-1
- Update to 0.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8-1
- Initial RPM release
