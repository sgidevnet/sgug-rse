%bcond_with tests
%bcond_with docs

%if 0%{?fedora} || 0%{?rhel} >= 8
%bcond_without python3
%else
%bcond_without python3
%endif

Name:       python-atomicwrites
Version:    1.3.0
Release:    2%{?git_tag}%{?dist}
Summary:    Python Atomic file writes on POSIX 

License:    MIT
URL:        https://github.com/untitaker/%{name}
Source0:    https://github.com/untitaker/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
%global short_name atomicwrites

BuildRequires:  python2-setuptools
%if %{with docs} && %{without python3}
BuildRequires:  python2-sphinx
%endif
%if %{with tests}
BuildRequires:  python2-pytest
%endif

%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with docs}
BuildRequires:  python3-sphinx
%endif
%if %{with tests}
BuildRequires:  python3-pytest
%endif
%endif


%global _description\
This Python module provides atomic file writes on POSIX operating systems.\
It sports:\
* Race-free assertion that the target file doesn''t yet exist\
* Windows support\
* Simple high-level API that wraps a very flexible class-based API

%description %_description

%package -n python2-%{short_name}
Summary: %summary
%{?python_provide:%python_provide python2-%{short_name}}

%description -n python2-%{short_name} %_description

%if %{with python3}
%package -n python3-%{short_name}
Summary:    Python Atomic file writes on POSIX 

%description -n python3-%{short_name}
This Python module provides atomic file writes on POSIX operating systems.
It sports:
* Race-free assertion that the target file doesn''t yet exist
* Windows support
* Simple high-level API that wraps a very flexible class-based API
%endif

%prep
%setup -q

%build
%{__python2} setup.py --quiet build

%if %{with docs} && %{without python3}
export PYTHONPATH=`pwd`
cd docs
make %{?_smp_mflags} man
cd ..
unset PYTHONPATH
%endif

%if %{with python3}
%py3_build

%if %{with docs}
export PYTHONPATH=`pwd`
cd docs
make %{?_smp_mflags} SPHINXBUILD=sphinx-build-3 man
cd ..
unset PYTHONPATH
%endif
%endif


%install
%{__python2} setup.py --quiet install -O1 --skip-build --root $RPM_BUILD_ROOT

%if %{with python3}
%py3_install
%endif

%if %{with docs}
install -d "$RPM_BUILD_ROOT%{_mandir}/man1"
cp -r docs/_build/man/*.1 "$RPM_BUILD_ROOT%{_mandir}/man1"
%endif

%check
%if %{with tests}
%{__python2} -m pytest -v

%if %{with python3}
%{__python3} -m pytest -v
%endif
%endif

%files -n python2-%{short_name}
%doc LICENSE README.rst
%{python2_sitelib}/*
%if %{with docs} && %{without python3}
%{_mandir}/man1/atomicwrites.1.*
%endif

%if %{with python3}
%files -n python3-%{short_name}
%doc README.rst LICENSE
%{python3_sitelib}/*
%if %{with docs}
%{_mandir}/man1/atomicwrites.1.*
%endif
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-12
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-10
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-9
- Bootstrap for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-8
- Remove unused tox dependency, use pytest
- Enable tests, they work without network
- Use python2 explicitly instead of python

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.5-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.5-5
- Python 2 binary package renamed to python2-atomicwrites
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-2
- Rebuild for Python 3.6

* Sun Sep 04 2016 Michele Baldessari <michele@acksyn.org> - 1.1.5-1
- New upstream release

* Wed Jul 27 2016 Michele Baldessari <michele@acksyn.org> - 1.1.0-1
- New upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Mar 26 2016 Michele Baldessari <michele@acksyn.org> - 1.0.0-1
- New upstream release

* Mon Feb 22 2016 Michele Baldessari <michele@acksyn.org> - 0.1.9-1
- New upstream release (BZ 1308379)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 13 2015 Michele Baldessari <michele@acksyn.org> - 0.1.8-1
- New upstream (BZ 1262584)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Michele Baldessari <michele@acksyn.org> - 0.1.5-1
- New upstream (BZ 1209294)

* Mon Mar 02 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-5
- Disable tests as they require network

* Sun Mar 01 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-4
- Move it to python 3

* Sat Feb 28 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-3
- Fix check section and add python-tox as BR

* Sat Feb 28 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-2
- Improve description

* Mon Feb 23 2015 Michele Baldessari <michele@redhat.com> - 0.1.4-1
- New upstream

* Wed Feb 04 2015 Michele Baldessari <michele@redhat.com> - 0.1.1-3
- Add python-sphinx BR

* Wed Oct 01 2014 Michele Baldessari <michele@redhat.com> - 0.1.1-1
- Initial packaging
