%global pkgname configparser
%global sum Backport of Python 3 configparser module

%if 0%{?fedora} || 0%{?rhel} > 7
  %global with_python3 1
  # Rename to python2-configparser after Fedora 23
  %global with_p2subpkg 1
%endif

# __python2 macro doesn't exist for el6
%if 0%{?el6}
  %define __python2 %{__python}
  %define python2_sitelib %{python_sitelib}
%endif

Name:           python-%{pkgname}
Version:        3.7.1
Release:        3%{?dist}
Summary:        %{sum}
License:        MIT
URL:            https://bitbucket.org/ambv/configparser
Source0:        %pypi_source %pkgname
BuildArch:      noarch

# For Fedora > 23 builds (protection against rename of python-setuptools)
%if 0%{?with_p2subpkg}
BuildRequires:  python2-devel python2-setuptools
Requires:       python2-setuptools
%else
BuildRequires:  python2-devel python-setuptools
Requires:       python-setuptools
Requires:       python2-backports
Provides:       python2-%{pkgname} = %{version}-%{release}
%endif

%if 0%{?with_python3}
BuildRequires:  python3-devel python3-setuptools
Requires:       python3-setuptools
%endif

%description
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.

# For Fedora > 23 builds
%if 0%{?with_p2subpkg}
%package -n python2-%{pkgname}
Summary:        %{sum}
Requires:       python2-backports
%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname}
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.
%endif

%if 0%{?with_python3}
%package -n python3-%{pkgname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.
%endif


%prep
%setup -q -n configparser-%{version}
rm -rf *.egg-info

# Python 2 setuptools cannot handle non-ASCII characters in setup.cfg.
# See https://github.com/pypa/setuptools/issues/1062
sed 's/Ł/L/' setup.cfg > setup.cfg.py2
cp -p setup.cfg setup.cfg.py3

%build
cp -p setup.cfg.py2 setup.cfg
%{__python2} setup.py build
%if 0%{?with_python3}
cp -p setup.cfg.py3 setup.cfg
%{__python3} setup.py build
%endif

%install
# The files are not executable anyway, so just delete the shebangs
rmshebangs() {
  for fil in $(grep -Frl '/usr/bin/env' $1); do
    sed -i.orig "\%/usr/bin/env%d" $fil
    touch -r $fil.orig $fil
    rm $fil.orig
  done
}

cp -p setup.cfg.py2 setup.cfg
%{__python2} setup.py install --skip-build --root %{buildroot}
rmshebangs %{buildroot}%{python2_sitelib}
rm %{buildroot}%{python2_sitelib}/backports/__init__.*
%if 0%{?with_python3}
cp -p setup.cfg.py3 setup.cfg
%{__python3} setup.py install --skip-build --root %{buildroot}
rmshebangs %{buildroot}%{python3_sitelib}
%endif

%check
cp -p setup.cfg.py2 setup.cfg
%{__python2} setup.py test
%if 0%{?with_python3}
cp -p setup.cfg.py3 setup.cfg
%{__python3} setup.py test
%endif

# For Fedora > 23 builds
%if 0%{?with_p2subpkg}
%files -n python2-%{pkgname}
%doc README.rst
%{python2_sitelib}/backports/configparser/
%{python2_sitelib}/configparser*
%else
%files
%doc README.rst
%{python2_sitelib}/backports/*
%{python2_sitelib}/configparser*
%endif

%if 0%{?with_python3}
%files -n python3-%{pkgname}
%doc README.rst
%{python3_sitelib}/*
%endif


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Jerry James <loganjerry@gmail.com> - 3.7.1-2
- Do not conflict with python2-backports

* Thu Feb 21 2019 Jerry James <loganjerry@gmail.com> - 3.7.1-1
- New upstream version
- Add workaround for https://github.com/pypa/setuptools/issues/1062
- Delete shebangs from nonexecutable files

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0b2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0b2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.0b2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0b2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 3.5.0b2-7
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0b2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0b2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.5.0b2-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0b2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0b2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Avram Lubkin <aviso@fedoraproject.org> - 3.5.0b2-1
- Updated to build for el6
- Updated to build Python3 packages
- Changed Python2 package name to python2-configparser for Fedora 24+
- Updated description
- Removed license comments

* Thu Jul 16 2015 José Matos <jamatos@fedoraproject.org> - 3.5.0b2-0.2
- Improve description to make it clear that this package in only needed for python 2.7
- Make the license tag information more explicit.

* Wed Jul 15 2015 José Matos <jamatos@fedoraproject.org> - 3.5.0b2-0.1
- First release for Fedora
