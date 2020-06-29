%global srcname minibelt
%global sum One-file utility module filled with helper functions for Python

Name:           python-%{srcname}
Version:        0.1.1
Release:        16%{?dist}
Summary:        One-file utility module filled with helper functions for Python

License:        zlib
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        http://pypi.python.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         minibelt-encoding.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
One-file utility module filled with helper functions for day to day
Python programming. This is a subset of batbelt, with only the most used
features, packed in a tiny file, and Python 2.7/3.3 compatible.

%package -n python3-%{srcname}
Summary:        One-file utility module filled with helper functions for Python
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
One-file utility module filled with helper functions for day to day
Python programming. This is a subset of batbelt, with only the most used
features, packed in a tiny file, and Python 2.7/3.3 compatible.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/minibelt*
%{python3_sitelib}/__pycache__/minibelt.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-14
- Subpackage python2-minibelt has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 13 2015 René Ribaud <rene.ribaud@free.fr> - 0.1.1-1
- Initial rpm
