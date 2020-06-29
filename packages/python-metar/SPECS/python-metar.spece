%global srcname metar
%global summary Coded METAR and SPECI weather reports parser for Python

Name: python-%{srcname}
Version: 1.7.0
Release: 6%{?dist}
Summary: %{summary}

License: BSD
URL: https://github.com/python-metar/python-metar
# note that development was moved to a new github account
# the old account was: http://github.com/tomp/python-metar
# see also this discussion on the 2 project names:
# https://github.com/python-metar/python-metar/issues/58
Source: https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel python3-pytest

%global _description \
Python-metar is a python package for interpreting METAR and SPECI coded \
weather reports.  METAR (Meteorological Aerodrome Report) and SPECI (Specials) \
are reports containing airport weather information encoded in ASCII \
following standards set by WMO (World Meteorological Organization) \
and ICAO (International Civil Aviation Organization).

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%build

%py3_build

%install

%py3_install

# note: sample file is not present anymore in pypi version
# remove executable permissions from sample.py to
# prevent dependencies being pulled in from this file
#chmod 644 sample.py

%check

# these variants dont work, even if the first one
# works just fine when doing a manual install. Dont know why.
#%%{__python3} setup.py test
#PYTHONPATH="%%{buildroot}%%{python3_sitelib}" %%{__python3} setup.py test

# this works fine
PYTHONPATH="%{buildroot}%{python3_sitelib}" %{_bindir}/pytest-3


%files -n python3-%{srcname}

%doc LICENSE README.md PKG-INFO CHANGELOG.md 
# sample.py

%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild


* Thu Mar 07 2019 Jos de Kloe <josdekloe@gmail.com> 1.7.0-1
- new upstream version and remove python2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Jos de Kloe <josdekloe@gmail.com> 1.6.0-1
- new upstream version and disable python2 sub-package for f30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Jos de Kloe <josdekloe@gmail.com> 1.5.0-3
- undo spec file name change since this seems not allowed

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Jos de Kloe <josdekloe@gmail.com> 1.5.0-1
- new upstream version and adapt to generate python2 and python3 versions

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Oct 08 2015 Jos de Kloe <josdekloe@gmail.com> 1.4.0-1
- Update to new upstream version and simplified spec file
- Add check section and run provided tests

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.0-4
- Rebuild for Python 2.6

* Thu Apr 24 2008 Matthias Saou <http://freshrpms.net/> 1.3.0-3
- Include everything under sitelib, to include egg files if present (F-9+).

* Tue Mar 27 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-2
- Include nobang patch.

* Fri Feb  9 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-1
- Initial RPM release.

