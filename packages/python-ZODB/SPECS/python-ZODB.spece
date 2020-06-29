%global srcname ZODB

Name:           python-%{srcname}
Version:        5.6.0
Release:        1%{?dist}
Summary:        Zope Object Database and persistence

License:        ZPLv2.1
URL:            http://www.zodb.org/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python-BTrees-doc
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3-persistent-devel
BuildRequires:  python3-persistent-doc
BuildRequires:  %{py3_dist btrees}
BuildRequires:  %{py3_dist j1m.sphinxautozconfig}
BuildRequires:  %{py3_dist manuel}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinxcontrib-zopeext}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist transaction}
BuildRequires:  %{py3_dist zc.lockfile}
BuildRequires:  %{py3_dist zconfig}
BuildRequires:  %{py3_dist zodbpickle}
BuildRequires:  %{py3_dist zope.testing}
BuildRequires:  %{py3_dist zope.testrunner}

%global common_desc                                                \
The ZODB package provides a set of tools for using the Zope Object \
Database (ZODB).

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        Zope Object Database and persistence
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%package doc
Summary:        Documentation for %{srcname}

%description doc
Documentation for %{srcname}.

%prep
%autosetup -n %{srcname}-%{version}

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -e "s|\('https://persistent\.readthedocs\.io/en/latest/', \)None|\1'%{_docdir}/python3-persistent-doc/objects.inv'|" \
    -e "s|\(\"https://btrees\.readthedocs\.io/en/latest/\", \)None|\1'%{_docdir}/python-BTrees-doc/objects.inv'|" \
    -i doc/conf.py

%build
%py3_build

# Build the documentation
cp -p doc/.static/zodb.ico doc
make -C doc html SPHINXBUILD=%{_bindir}/sphinx-build PYTHONPATH=$PWD/src
rm doc/build/html/.buildinfo
rst2html --no-datestamp CHANGES.rst CHANGES.html

%install
%py3_install

# Fix scripts
for script in \
  $(grep -l '^#!' %{buildroot}%{python3_sitelib}/%{srcname}/scripts/*.py); do
  sed 's,%{_bindir}/python,&3,;s,%{_bindir}/env python.*,%{_bindir}/python3,' \
    $script > $script.new
  touch -r $script $script.new
  mv -f $script.new $script
  chmod 0755 $script
done

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest

%files -n python3-%{srcname}
%license COPYRIGHT.txt LICENSE.txt
%doc CHANGES.html
%{_bindir}/fsdump
%{_bindir}/fsoids
%{_bindir}/fsrefs
%{_bindir}/fstail
%{_bindir}/repozo
%{python3_sitelib}/%{srcname}*

%files doc
%doc doc/build/html

%changelog
* Tue Jun 16 2020 Jerry James <loganjerry@gmail.com> - 5.6.0-1
- Version 5.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 5.5.1-1
- New upstream release
- Drop the python2 subpackage

* Thu Sep 13 2018 Jerry James <loganjerry@gmail.com> - 5.4.0-4
- Build documentation again, in the -doc subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.4.0-2
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Jerry James <loganjerry@gmail.com> - 5.4.0-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct  7 2017 Jerry James <loganjerry@gmail.com> - 5.3.0-1
- New upstream release
- Skip doc building until new dependencies can be added to Fedora

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-2
- Rebuild for Python 3.6

* Sat Dec 10 2016 Jerry James <loganjerry@gmail.com> - 5.1.1-1
- New upstream release

* Tue Sep  6 2016 Jerry James <loganjerry@gmail.com> - 5.0.0-1
- New upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 10 2016 Jerry James <loganjerry@gmail.com> - 4.3.1-1
- New upstream release

* Wed Jun  1 2016 Jerry James <loganjerry@gmail.com> - 4.3.0-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 4.2.0-3
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  9 2015 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- New upstream release

* Mon Jan 12 2015 Jerry James <loganjerry@gmail.com> - 4.1.0-1
- New upstream release

* Wed Aug  6 2014 Jerry James <loganjerry@gmail.com> - 4.0.1-1
- New upstream release

* Wed Jun 11 2014 Jerry James <loganjerry@gmail.com> - 4.0.0-1
- Initial RPM
