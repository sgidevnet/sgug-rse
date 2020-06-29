%if 0%{?fedora}
%else
%global with_python3 0
%endif

Name:           python-gccinvocation
Version:        0.1
Release:        24%{?dist}
Summary:        Library for parsing GCC command-line options

License:        LGPLv2+
URL:            https://github.com/fedora-static-analysis/gccinvocation
Source0:        https://pypi.python.org/packages/source/g/gccinvocation/gccinvocation-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# ^^^: used during selftests

%global _description\
"gccinvocation" is a python module that can parse gcc command lines and\
extract data of interest e.g. include paths, defines, etc.

%description %_description

%package -n python3-gccinvocation
Summary:        Library for parsing GCC command-line options

%description -n python3-gccinvocation
"gccinvocation" is a python module that can parse gcc command lines and
extract data of interest e.g. include paths, defines, etc.


%prep
%setup -q -n gccinvocation-%{version}



%build

%{__python3} setup.py build


%install

%{__python3} setup.py install --skip-build --root %{buildroot}


%check
%{__python3} gccinvocation.py -v


%files -n python3-gccinvocation
%doc README.rst lgpl-2.1.txt
%{python3_sitelib}/gccinvocation-%{version}-py3.?.egg-info
%{python3_sitelib}/gccinvocation.py
%{python3_sitelib}/__pycache__/gccinvocation.cpython-*.py[co]


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1-18
- Subpackage python2-gccinvocation has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 20 2018 David Malcolm <dmalcolm@redhat.com> - 0.1-17
- Use explicit "python2" versions of specfile macros (rhbz #1605703)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-15
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1-13
- Python 2 binary package renamed to python2-gccinvocation
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 David Malcolm <dmalcolm@redhat.com> - 0.1-2
- remove redundant clean of buildroot from install phase; change BR from
python-devel to python2-devel; add trailing period to description

* Fri May 31 2013 David Malcolm <dmalcolm@redhat.com> - 0.1-1
- initial packaging

