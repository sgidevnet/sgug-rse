# https://bugzilla.redhat.com/show_bug.cgi?id=998047

Name:           python-backports
Version:        1.0
Release:        17%{?dist}
Summary:        Namespace for backported Python features

# Only code is sourced from http://www.python.org/dev/peps/pep-0382/
License:        Public Domain
URL:            https://pypi.python.org/pypi/backports
Source0:        backports.py

BuildRequires:  python2-devel

%global _description\
The backports namespace is a namespace reserved for features backported from\
the Python standard library to older versions of Python 2.\
\
Packages that exist in the backports namespace in Fedora should not provide\
their own backports/__init__.py, but instead require this package.\
\
Backports to earlier versions of Python 3, if they exist, do not need this\
package because of changes made in Python 3.3 in PEP 420\
(http://www.python.org/dev/peps/pep-0420/).\


%description %_description

%package -n python2-backports
Summary: %summary
%{?python_provide:%python_provide python2-backports}

%description -n python2-backports %_description

%prep


%build


%install
mkdir -pm 755 %{buildroot}%{python2_sitelib}/backports
install -pm 644 %{SOURCE0} %{buildroot}%{python2_sitelib}/backports/__init__.py
%if "%{python2_sitelib}" != "%{python2_sitearch}"
mkdir -pm 755 %{buildroot}%{python2_sitearch}/backports
install -pm 644 %{SOURCE0} %{buildroot}%{python2_sitearch}/backports/__init__.py
%endif

 
%files -n python2-backports
%{python2_sitelib}/backports
%if "%{python2_sitelib}" != "%{python2_sitearch}"
%{python2_sitearch}/backports
%endif


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-15
- Use versioned python sitelib/arch macros

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-12
- Python 2 binary package renamed to python2-backports
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Ian Weller <iweller@redhat.com> - 1.0-3
- Install to both python_sitelib and python_sitearch

* Mon Aug 19 2013 Ian Weller <iweller@redhat.com> - 1.0-2
- Install to the correct location

* Fri Aug 16 2013 Ian Weller <iweller@redhat.com> - 1.0-1
- Initial package build
