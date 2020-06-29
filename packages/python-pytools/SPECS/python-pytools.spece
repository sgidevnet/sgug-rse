%{?python_enable_dependency_generator}

%global srcname pytools

Name:           python-%{srcname}
Version:        2019.1
Release:        7%{?dist}
Summary:        Collection of tools for Python

License:        MIT
URL:            https://pypi.python.org/pypi/pytools
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description \
Pytools is a big bag of things that are "missing" from the Python standard\
library. This is mainly a dependency of my other software packages, and is\
probably of little interest to you unless you use those. If you're curious\
nonetheless, here's what's on offer:\
\
  * A ton of small tool functions such as `len_iterable`, `argmin`,\
    tuple generation, permutation generation, ASCII table pretty printing,\
    GvR's mokeypatch_xxx() hack, the elusive `flatten`, and much more.\
  * Michele Simionato's decorator module\
  * A time-series logging module, `pytools.log`.\
  * Batch job submission, `pytools.batchjob`.\
  * A lexer, `pytools.lex`.

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3dist(decorator) >= 3.2
BuildRequires:  python3dist(appdirs) >= 1.4
BuildRequires:  python3dist(six) >= 1.8
BuildRequires:  python3dist(numpy) >= 1.6
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v
 
%files -n python3-%{srcname}
%license LICENSE
%doc README.rst PKG-INFO
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2019.1-1
- Update to 2019.1

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.5.2-4
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.5.2-2
- Rebuilt for Python 3.7

* Sun Jul 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2018.5.2-1
- Update to 2018.5.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.2-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2018.2-1
- Update to 2018.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.6-1
- Update to 2017.6

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.4-1
- Update to 2017.4

* Sat Jul 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 2017.3-1
- Update to 2017.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2016.2.6-2
- Rebuild for Python 3.6

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2016.2.6-1
- Update to 2016.2.6

* Mon Oct 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2016.2.4-1
- Update to 2016.2.4
- Fixes in spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.1.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 05 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2015.1.2-1
- Update to 2015.1.2
- Update python macroses
- Add python3 subpackage
- Update for new python packaging guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 09 2009 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> 8-2
- Spec file cleanup 

* Wed Apr 08 2009 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> 8-1
- Initial RPM release
