%global modname pypng

Name:               python-pypng
Version:            0.0.18
Release:            19%{?dist}
Summary:            Pure Python PNG image encoder/decoder

License:            MIT
URL:                http://pypi.python.org/pypi/pypng
Source0:            https://github.com/drj11/%{modname}/archive/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      /usr/bin/2to3
BuildRequires:      python3-devel
BuildRequires:      python3-nose

%global _description\
PyPNG allows PNG image files to be read and written using pure Python.\
\
It's available from github.com https://github.com/drj11/pypng\
\
Documentation is kindly hosted by PyPI http://pythonhosted.org/pypng/

%description %_description

%package -n python3-pypng
Summary:            Pure Python PNG image encoder/decoder
%{?python_provide:%python_provide python3-pypng}

%description -n python3-pypng
PyPNG allows PNG image files to be read and written using pure Python.

It's available from github.com https://github.com/drj11/pypng

Documentation is kindly hosted by PyPI http://pythonhosted.org/pypng/

%prep
%setup -q -n %{modname}-%{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

# Remove the shebang from the main lib
lib=code/png.py
sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
touch -r $lib $lib.new &&
mv $lib.new $lib

2to3 --write --nobackups .

%build
%py3_build

%install
%py3_install

%check
nosetests-3 code/png.py

%files -n python3-pypng
%doc README.txt LICENCE
%{python3_sitelib}/png.py*
%{python3_sitelib}/__pycache__/png*
%{python3_sitelib}/%{modname}-%{version}-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.18-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.18-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.18-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.18-13
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.18-11
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.0.18-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.18-8
- Python 2 binary package renamed to python2-pypng
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.18-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Aug 01 2015 Ralph Bean <rbean@redhat.com> - 0.0.18-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Ralph Bean <rbean@redhat.com> - 0.0.17-1
- new version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri May 09 2014 Ralph Bean <rbean@redhat.com> - 0.0.16-1
- initial package for Fedora
