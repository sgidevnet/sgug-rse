%global srcname snuggs

Name:           python-%{srcname}
Version:        1.4.7
Release:        3%{?dist}
Summary:        Snuggs are S-expressions for Numpy

License:        MIT
URL:            https://github.com/mapbox/snuggs
Source0:        %pypi_source

BuildArch:      noarch

%global _description \
Snuggs are S-expressions for NumPy. Snuggs wraps NumPy in expressions with the \
following syntax: expression "(" (operator | function) *arg ")" where \
arg = expression | name | number | string

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy
BuildRequires:  python3-pyparsing >= 2.1.6
BuildRequires:  python3-hypothesis

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info PKG-INFO


%build
%py3_build


%install
%py3_install


%check
pytest-3 -v


%files -n python3-%{srcname}
%doc README.rst AUTHORS.txt CHANGES.txt
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.7-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.7-1
- Update to latest version

* Sun Aug 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.6-3
- Patch tests to work with pyparsing 2.4+

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.6-1
- Update to latest version

* Tue May 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.5-1
- Update to latest version

* Mon Feb 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-2
- Remove extra click dependency
- Remove explicit dependencies and use the generator

* Mon Feb 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-4
- Drop Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.7

* Thu Jun 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-1
- Update to latest version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Initial package.
