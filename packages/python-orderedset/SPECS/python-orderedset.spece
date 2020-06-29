%global srcname orderedset
%global user simonpercivall

Name:           python-%{srcname}
Version:        2.0.3
Release:        2%{?dist}
Summary:        Ordered set implementation in Cython

License:        BSD
URL:            https://github.com/%{user}/%{srcname}
Source0:        %pypi_source
# https://github.com/simonpercivall/orderedset/pull/22
Patch0:         %{name}-comparison.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(setuptools)

%global common_desc \
This package contains an ordered set implementation in Cython.  Features:\
- Works like a regular set, but remembers insertion order;\
- Is approximately 5 times faster than the pure Python implementation\
  overall (and 5 times slower than set);\
- Compatible with Python 2.6 through 3.6.;\
- Supports the full set interface;\
- Supports some list methods, like index and __getitem__.\
- Supports set methods against iterables.

%description
%common_desc

%package -n python3-%{srcname}
Summary:        Ordered set implementation in Cython

Provides:       bundled(jquery)
Provides:       bundled(js-underscore)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%common_desc

%prep
%autosetup -n %{srcname}-%{version} -p1

# Set the language level
sed -i "s/pyx'])/&, compiler_directives={'language_level': 3}/" setup.py

%build
%py3_build
rst2html --no-datestamp AUTHORS.rst AUTHORS.html
rst2html --no-datestamp HISTORY.rst HISTORY.html
rst2html --no-datestamp README.rst README.html

%install
%py3_install
chmod 0755 %{buildroot}%{python3_sitearch}/%{srcname}/*.so

%check
PYTHONPATH=$PWD %{__python3} setup.py test

%files -n python3-%{srcname}
%doc AUTHORS.html HISTORY.html README.html
%license LICENSE
%{python3_sitearch}/%{srcname}*

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Rebuilt for Python 3.9

* Wed Feb 26 2020 Jerry James <loganjerry@gmail.com> - 2.0.3-1
- Version 2.0.3

* Tue Feb 25 2020 Jerry James <loganjerry@gmail.com> - 2.0.2-1
- Version 2.0.2
- Drop upstreamed -python38 patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Jerry James <loganjerry@gmail.com> - 2.0.1-9
- Add -comparison and -python38 patches to fix FTBFS in Rawhide
- Set the Cython language level to 3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Jerry James <loganjerry@gmail.com> - 2.0.1-4
- Drop python2 subpackage (bz 1645073)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.7

* Mon Apr 30 2018 Jerry James <loganjerry@gmail.com> - 2.0.1-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 25 2016 Jerry James <loganjerry@gmail.com> - 2.0-1
- Initial RPM
