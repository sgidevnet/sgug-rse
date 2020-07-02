%global srcname yappi

# python3 is enabled in any fedora and rhel>7
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%else
%global with_python3 0
%endif

# python2 is disabled only in fedora >= 30
%if 0%{?fedora} >= 30 
%global with_python2 0
%else
%global with_python2 1
%endif

Name:           python-%{srcname}
Version:        1.0
Release:        6%{?dist}
Summary:        Yet Another Python Profiler, supports Multithread/CPU time profiling

License:        MIT
URL:            https://github.com/sumerc/yappi
Source0:        https://files.pythonhosted.org/packages/source/y/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc

%description
Yappi, Yet Another Python Profiler, provides multithreading and cpu-time
support to profile python programs.

%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        Yet Another Python Profiler, supports Multithread/CPU time profiling.
%{?python_provide:%python_provide python2-%{srcname}}

# Previously bundled things:
BuildRequires:       python2-devel
BuildRequires:       python2-setuptools

%description -n python2-%{srcname}
Yappi, Yet Another Python Profiler, provides multithreading and cpu-time
support to profile python programs.

%endif

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        Yet Another Python Profiler, supports Multithread/CPU time profiling.

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname}
Yappi, Yet Another Python Profiler, provides multithreading and cpu-time
support to profile python programs.

%endif

%prep
%autosetup -n %{srcname}-%{version} -S git

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
mv %{buildroot}%{_bindir}/%{srcname} %{buildroot}%{_bindir}/%{srcname}-%{python2_version}
ln -s %{srcname}-%{python2_version} %{buildroot}%{_bindir}/%{srcname}-2
ln -s %{srcname}-2 %{buildroot}%{_bindir}/%{srcname}
%endif
%if 0%{?with_python3}
rm -f %{buildroot}%{_bindir}/%{srcname}
%py3_install
mv %{buildroot}%{_bindir}/%{srcname} %{buildroot}%{_bindir}/%{srcname}-%{python3_version}
ln -s %{srcname}-%{python3_version} %{buildroot}%{_bindir}/%{srcname}-3
ln -s %{srcname}-3 %{buildroot}%{_bindir}/%{srcname}
%endif

%check
%if 0%{?with_python2}
export PYTHONPATH=%{buildroot}/%{python2_sitearch}
%{__python2} tests/test_functionality.py
%{__python2} tests/test_hooks.py
%endif
%if 0%{?with_python3}
export PYTHONPATH=%{buildroot}/%{python3_sitearch}
%{__python3} tests/test_functionality.py
%{__python3} tests/test_hooks.py
%endif

%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitearch}/%{srcname}.py*
%{python2_sitearch}/_%{srcname}.so
%{python2_sitearch}/%{srcname}-*.egg-info
%{_bindir}/%{srcname}-2*
%if 0%{?with_python3} == 0
%{_bindir}/%{srcname}
%endif
%endif


%if 0%{?with_python3}
%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{srcname}.py*
%{python3_sitearch}/_%{srcname}*.so
%{python3_sitearch}/__pycache__/%{srcname}*
%{python3_sitearch}/%{srcname}-*.egg-info
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-3*
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.0-1
- Initial version
