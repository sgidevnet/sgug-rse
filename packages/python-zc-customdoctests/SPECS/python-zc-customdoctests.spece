
%global modname zc.customdoctests

Name:               python-zc-customdoctests
Version:            1.0.1
Release:            24%{?dist}
Summary:            Use doctest with other languages
License:            ZPLv2.1
URL:                http://pypi.python.org/pypi/zc.customdoctests
Source0:            http://pypi.python.org/packages/source/z/%{modname}/%{modname}-%{version}.zip

BuildArch:          noarch


%if 0%{?rhel}
# No tests on rhel
%endif

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-zope-testing
BuildRequires:      python3-manuel
BuildRequires:      python3-six

%global _description\
doctest (and recently manuel) provide hooks for using custom doctest\
parsers.  `zc.customdoctests` helps to leverage this to support other\
languages, such as JavaScript::\
\
js> function double (x) { ...     return x*2; ... } js> double(2) 4\
\
And with manuel, it facilitates doctests that mix multiple languages,\
such as Python, JavaScript, and sh.

%description %_description

%package -n python3-zc-customdoctests
Summary:            Use doctest with other languages

%description -n python3-zc-customdoctests
doctest (and recently manuel) provide hooks for using custom doctest
parsers.  `zc.customdoctests` helps to leverage this to support other
languages, such as JavaScript::

js> function double (x) { ...     return x*2; ... } js> double(2) 4

And with manuel, it facilitates doctests that mix multiple languages,
such as Python, JavaScript, and sh.

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}

%check
%if 0%{?rhel}
# No tests on rhel
%else
%{__python3} setup.py test
%endif

%files -n python3-zc-customdoctests
%doc README.txt CHANGES.txt PKG-INFO
%{python3_sitelib}/zc/customdoctests/
%{python3_sitelib}/%{modname}-%{version}-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-19
- Subpackage python2-zc-customdoctests has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-16
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.1-13
- Python 2 binary package renamed to python2-zc-customdoctests
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Ralph Bean <rbean@redhat.com> - 1.0.1-2
- Removed tests on rhel: no python-manuel available.

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- Initial package for Fedora
