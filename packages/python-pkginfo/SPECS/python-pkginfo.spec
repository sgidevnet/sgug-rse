%global srcname pkginfo
%global sum Query metadata from sdists / bdists / installed packages

Name:           python-%{srcname}
Version:        1.4.2
Release:        5%{?dist}
Summary:        %{sum}

# License is missing from the source repo: see https://bugs.launchpad.net/pkginfo/+bug/1591344
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/pkginfo/pkginfo-%{version}.tar.gz
# Upstream installs the test package, and we don't need to distribute that.
Patch0:         0001-Stop-installing-the-test-package.patch

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel
BuildRequires:  python2-nose python3-nose
BuildRequires:  python3-sphinx


%description
This package provides an API for querying the distutils metadata written in the
PKG-INFO file inside a source distribution (an sdist) or a binary distribution
(e.g., created by running bdist_egg). It can also query the EGG-INFO directory
of an installed distribution, and the *.egg-info stored in a "development
checkout" (e.g, created by running setup.py develop).


%package -n python2-%{srcname}
Summary:        %{sum}
Requires:       python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This package provides an API for querying the distutils metadata written in the
PKG-INFO file inside a source distribution (an sdist) or a binary distribution
(e.g., created by running bdist_egg). It can also query the EGG-INFO directory
of an installed distribution, and the *.egg-info stored in a "development
checkout" (e.g, created by running setup.py develop).


%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This package provides an API for querying the distutils metadata written in the
PKG-INFO file inside a source distribution (an sdist) or a binary distribution
(e.g., created by running bdist_egg). It can also query the EGG-INFO directory
of an installed distribution, and the *.egg-info stored in a "development
checkout" (e.g, created by running setup.py develop).


%package -n python-%{srcname}-doc
Summary:        Documentation for the python-%{srcname} packages

%description -n python-%{srcname}-doc
This package provides documentation for the Python pkginfo package. pkginfo
provides an API for querying the distutils metadata written in the PKG-INFO
file inside a source distribution (an sdist) or a binary distribution (e.g.,
created by running bdist_egg). It can also query the EGG-INFO directory of an
installed distribution, and the *.egg-info stored in a "development checkout"
(e.g, created by running setup.py develop).


%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf *.egg-info


%build
%py2_build
%py3_build

cd docs
make %{?_smp_mflags} SPHINXBUILD=sphinx-build-3 html
rm .build/html/objects.inv

%install
# Provide both Python 3 and Python 2 binary entries
%py3_install
mv %{buildroot}%{_bindir}/pkginfo %{buildroot}%{_bindir}/pkginfo-%{python3_version}
ln -s %{_bindir}/pkginfo-%{python3_version} %{buildroot}%{_bindir}/pkginfo-3

%py2_install
ln -s %{_bindir}/pkginfo %{buildroot}%{_bindir}/pkginfo-%{python2_version}
ln -s %{_bindir}/pkginfo-%{python2_version} %{buildroot}%{_bindir}/pkginfo-2


# Upstream ships a broken unit test: see https://bugs.launchpad.net/pkginfo/+bug/1591298
# Until that's fixed, skip testing.


%files -n python2-%{srcname}
%doc README.txt CHANGES.txt
%{python2_sitelib}/*
%{_bindir}/pkginfo
%{_bindir}/pkginfo-2
%{_bindir}/pkginfo-%{python2_version}

%files -n python3-%{srcname}
%doc README.txt CHANGES.txt
%{python3_sitelib}/*
%{_bindir}/pkginfo-3
%{_bindir}/pkginfo-%{python3_version}

%files -n python-%{srcname}-doc
%doc README.txt CHANGES.txt
%doc docs/.build/html/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.7

* Sat Mar 24 2018 Jeremy Cline <jeremy@jcline.org> - 1.4.2-1
- Update to latest upstream
- License change to MIT

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-4
- Rebuild for Python 3.6

* Wed Jul 20 2016 Jeremy Cline <jeremy@jcline.org> - 1.3.2-3
- Remove hard-coded Python y release versions in /usr/bin entries

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 09 2016 Jeremy Cline <jeremy@jcline.org> - 1.3.2-1
- Initial commit
