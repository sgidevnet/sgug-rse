%global srcname Unidecode

Name:		python-unidecode
Version:	1.0.22
Release:	10%{?dist}
Summary:	US-ASCII transliterations of Unicode text

License:	GPLv2+
URL:		https://pypi.python.org/pypi/%{srcname}/%{version}
Source0:	https://files.pythonhosted.org/packages/source/U/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch

%global _description\
This is a python port of Text::Unidecode Perl module. It provides a function,\
'unidecode(...)' that takes Unicode data and tries to represent it in ASCII\
characters.

%description %_description


%package -n python3-unidecode
Summary:	US-ASCII transliterations of Unicode text
BuildRequires: python3-devel

%{?python_provide:%python_provide python3-unidecode}

%description -n python3-unidecode
This is a python port of Text::Unidecode Perl module. It provides a function,
'unidecode(...)' that takes Unicode data and tries to represent it in ASCII
characters.


%prep
%setup -q -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-unidecode
%license LICENSE
%doc README.rst ChangeLog
%{_bindir}/unidecode
%{python3_sitelib}/unidecode/
%{python3_sitelib}/*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.22-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.22-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.22-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.22-5
- Subpackage python2-unidecode has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.22-2
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.0.22-1
- Update to 1.0.22
- Don't build Python 2 subpackage on EL > 7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.04.16-10
- Python 2 binary package renamed to python2-unidecode
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.04.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.04.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.04.16-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04.16-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.04.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04.16-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Sep 07 2014 P J P <pjp@fedoraproject.org> - 0.04.16-2
- Fixed python3-unidecode build to make it conditional on epel.

* Tue Sep 02 2014 P J P <pjp@fedoraproject.org> - 0.04.16-1
- New release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.04.13-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.04.13-1
- new upstream release
- python 3 build. resolves rhbz#975711

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.04.7-7
- This package does not use setuptools.  Remove the BR for that.  Also correct the
  %%files list -- The egg-info is a file, not a directory (b/c it is created by
  distutils, not by setuptools.)  Older rpms fixed up the entry behind the
  scenes.  Newer ones fail so we need to correct it explicitly.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.04.7-4
- mark it noarch.  Pointed out Ville Skyttä

* Fri Jul 15 2011 P J P <pj.pandit@yahoo.co.in> - 0.04.7-3
- changed to use srcname and version macros in URL & Source0 variables.

* Tue Jul 12 2011 P J P <pj.pandit@yahoo.co.in> - 0.04.7-2
- added BuildRequires, and changed description to be more concise.

* Mon Jul 11 2011 P J P <pj.pandit@yahoo.co.in> - 0.04.7-1
- Initial RPM for python-unidecode.
