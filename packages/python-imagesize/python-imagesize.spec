
%global pypi_name imagesize
%global sum  Python module for analyzing image file headers and returning image sizes

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/shibukawa/imagesize_py
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
The imagesize package parses image file headers and returns the image sizes.

* PNG
* JPEG
* JPEG2000
* GIF

This is a pure Python library.

%package -n     python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The imagesize package parses image file headers and returns the image sizes.

* PNG
* JPEG
* JPEG2000
* GIF

This is a pure Python library.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
py.test-3

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.rst
%{python3_sitelib}/imagesize*
%{python3_sitelib}/__pycache__/imagesize*

%changelog
* Mon Oct 28 2019 Avram Lubkin <aviso@rockhopper.net> - 1.1.0-1
- Updated to 1.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-5
- Subpackage python2-imagesize has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Avram Lubkin <aviso@rockhopper.net> - 1.0.0-1
- Updated to 1.0.0 (bz#1545961)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.7.1-4
- Enable tests

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.7.1-3
- Rebuild for Python 3.6
- Disable python3 tests

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 26 2016 Avram Lubkin <aviso@rockhopper.net> - 0.7.1-1
- Initial package.
