%if 0%{?fedora} < 31
%global         py2 1
%endif

Summary:       Debugger using ptrace written in Python
Name:          python-ptrace
Version:       0.9.5
Release:       2%{?dist}
License:       GPLv2
URL:           https://bitbucket.org/haypo/python-ptrace
Source0:       https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires: gcc
%if 0%{?py2}
BuildRequires: python2-devel
BuildRequires: python2-setuptools
%endif
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%global _description \
python-ptrace is a debugger using ptrace written in Python. \
Features: \
 o High level Python object API : PtraceDebugger and PtraceProcess \
 o Able to control multiple processes: catch fork events on Linux \
 o Read/write bytes to arbitrary address: take care of memory alignment \
   and split bytes to cpu word \
 o Execution step by step using ptrace_singlestep() \
   or hardware interruption 3 \
 o Dump registers, memory mappings, stack, etc. \
 o Syscall tracer and parser (strace.py command) \
 o Can use distorm disassembler (if available)
%description %_description

%package    -n python2-ptrace
Summary:       Debugger using ptrace written in Python 2
%{?python_provide:%python_provide python2-ptrace}
%description -n python2-ptrace %_description

%package    -n python3-ptrace
Summary:       Debugger using ptrace written in Python 3
%{?python_provide:%python_provide python3-ptrace}
%description -n python3-ptrace %_description

%prep
%setup -q
chmod 0644 examples/*.py

%build
%if 0%{?py2}
%{py2_build}
%{__python2} setup_cptrace.py build
%endif
%{py3_build}
%{__python3} setup_cptrace.py build

%install
%if 0%{?py2}
%{py2_install}
%{__python2} setup_cptrace.py install -O1 --skip-build --root %{buildroot}
for f in gdb strace ; do
    rm -f %{buildroot}%{_bindir}/$f.{pyo,pyc}
    mv %{buildroot}%{_bindir}/$f.py  %{buildroot}%{_bindir}/$f-python2.py 
done
%endif
%{py3_install}
%{__python3} setup_cptrace.py install -O1 --skip-build --root %{buildroot}

rm -f %{buildroot}%{_bindir}/{gdb,strace}.{pyo,pyc}

%check
%{?py2:%{__python2} runtests.py || :}
%{__python3} runtests.py || :

%if 0%{?py2}
%files -n python2-ptrace
%license COPYING
%doc README.rst
%doc doc/* examples
%{_bindir}/gdb-python2.py
%{_bindir}/strace-python2.py
%{python2_sitelib}/ptrace/
%{python2_sitelib}/python_ptrace-*-py*.egg-info
%{python2_sitearch}/cptrace.so
%{python2_sitearch}/cptrace-*-py*.egg-info
%endif

%files -n python3-ptrace
%license COPYING
%doc README.rst
%doc doc/* examples
%{_bindir}/gdb.py
%{_bindir}/strace.py
%{python3_sitelib}/ptrace/
%{python3_sitelib}/python_ptrace-*-py*.egg-info
%{python3_sitearch}/cptrace.cpython-*.so
%{python3_sitearch}/cptrace-*-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.9.5-1
- 0.9.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-3
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-2
- No Python 2 in newer Fedoras

* Sun Aug 18 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-1
- 0.9.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.9.3-6
- Use correct python macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Oct 01 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.9.3-1
- 0.9.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 09 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.9.2-1
- 0.9.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-1
- 0.8.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.6-5
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Jan 20 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.6.6-2
- Patch still needed

* Mon Jan 20 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.6.6-1
- 0.6.6

* Sun Oct 27 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.6.5-1
- 0.6.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.6.4-2
- Add patch to build with Python 3.3

* Wed Dec 05 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.6.4-1
- 0.6.4
- Add python 3 subpackage

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.6.3-1
- 0.6.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 11 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Dec 05 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6.2-1
- 0.6.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  8 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6-4
- Build with all rpm versions

* Sun Mar  8 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6-3
- Remove %%exclude

* Thu Mar  5 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6-2
- switch to %%global, fix files listing, remove comments

* Wed Mar  4 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.6-1
- 0.6

* Sat Sep 13 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.5-1
- 0.5
