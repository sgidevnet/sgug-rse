# Created by pyp2rpm-2.0.0
%global pypi_name rjsmin

Name:           python-%{pypi_name}
Version:        1.0.12
Release:        15%{?dist}
Summary:        Javascript Minifier

License:        ASL 2.0
URL:            http://opensource.perlig.de/rjsmin/
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  gcc

%description
rJSmin is a javascript minifier written in python.

The minifier is based on the semantics
of jsmin.c by Douglas Crockford.

The module is a re-implementation aiming
for speed, so it can be used at
runtime (rather than during a preprocessing
step). Usually it produces the
same results as the original jsmin.c.

%package -n     python3-%{pypi_name}
Summary:        Javascript Minifier
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
rJSmin is a javascript minifier written in python.

The minifier is based on the semantics
of jsmin.c by Douglas Crockford.

The module is a re-implementation aiming
for speed, so it can be used at
runtime (rather than during a preprocessing
step). Usually it produces the
same results as the original jsmin.c.

%package docs
Summary:    Javascript Minifier - docs
%description docs
Docs for rJSmin, which is a javascript minifier written in python.

The minifier is based on the semantics
of jsmin.c by Douglas Crockford.

The module is a re-implementation aiming
for speed, so it can be used at
runtime (rather than during a preprocessing
step). Usually it produces the
same results as the original jsmin.c.



%prep
%autosetup -n %{pypi_name}-%{version}

# strip bang path from rjsmin.py
sed -i '1d' rjsmin.py

%build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install


# remove upstream developer documentation
rm -r %{buildroot}/%{_docdir}/%{pypi_name}/

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitearch}/%{pypi_name}.py
%{python3_sitearch}/_%{pypi_name}.cpython*
%{python3_sitearch}/__pycache__/rjsmin.*
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files docs
%doc README.rst docs

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.12-13
- Subpackage python2-rjsmin has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.12-11
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Matthias Runge <mrunge@redhat.com> - 1.0.12-10
- add gcc build requirement

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.12-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.12-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.12-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 15 2016 Matthias Runge <mrunge@redhat.com> - 1.0.12-2
- split out -docs package, clean up description (rhbz#1312350)

* Fri Feb 26 2016 Matthias Runge <mrunge@redhat.com> - 1.0.12-1
- Initial package. (rhbz#1312350)
