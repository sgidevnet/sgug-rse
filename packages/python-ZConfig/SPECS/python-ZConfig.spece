Name:           python-ZConfig
Version:        3.1.0
Release:        19%{?dist}
Summary:        Structured Configuration Library
License:        ZPLv2.1
URL:            http://www.zope.org/Members/fdrake/zconfig/
Source0:        http://pypi.python.org/packages/source/Z/ZConfig/ZConfig-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# for tests, not available in Fedora
#BuildRequires:  python3-zope-testrunner

%description
ZConfig is a configuration library intended for general use. It supports
a hierarchical schema-driven configuration model that allows a schema to
specify data conversion routines written in Python. ZConfig's model is
very different from the model supported by the ConfigParser module found
in Python's standard library, and is more suitable to
configuration-intensive applications.

%package -n python3-ZConfig
Summary:        Structured Configuration Library
%{?python_provide:%python_provide python3-ZConfig}
Conflicts:      python2-ZConfig < 3.1.0-14

%description -n python3-ZConfig
ZConfig is a configuration library intended for general use. It supports
a hierarchical schema-driven configuration model that allows a schema to
specify data conversion routines written in Python. ZConfig's model is
very different from the model supported by the ConfigParser module found
in Python's standard library, and is more suitable to
configuration-intensive applications.


%prep
%setup -q -n ZConfig-%{version}


%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
rm -f %{buildroot}%{python3_sitelib}/ZConfig/*.txt

#%%check
#%%{__python3} setup.py test

%files -n python3-ZConfig
%doc README.txt doc/zconfig.pdf ZConfig/*.txt
%license COPYRIGHT.txt LICENSE.txt
%{python3_sitelib}/*
%exclude %{python3_sitelib}/ZConfig/tests/
%{_bindir}/zconfig
%{_bindir}/zconfig_schema2html


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-14
- Subpackage python2-ZConfig has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.0-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Ralph Bean <rbean@redhat.com> - 3.1.0-3
- Modernize python macros.
- Provide explicit python2 subpackage.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Oct 18 2015 Ralph Bean <rbean@redhat.com> - 3.1.0-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 10 2014 Ralph Bean <rbean@redhat.com> - 3.0.4-1
- Latest upstream.
- Added python3 subpackage.
- Modernized python2 macros
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Robin Lee <cheeselee@fedoraproject.org> - 2.9.2-1
- Update to 2.9.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 30 2011 Robin Lee <cheeselee@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0 (#689762)
- Exclude the tests

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jun 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 2.8.0-3
- Workaround of installation

* Wed Jun 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 2.8.0-2
- Retag

* Wed Jun 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 2.8.0-1
- 2.8.0
- BR: python-zope-testing removed
- More docs included

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Conrad Meyer <konrad@tylerc.org> - 2.7.1-1
- New version.

* Sun Dec 14 2008 Conrad Meyer <konrad@tylerc.org> - 2.6.1-1
- Initial package.
