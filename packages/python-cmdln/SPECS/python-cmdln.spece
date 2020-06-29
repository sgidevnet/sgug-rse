%global commit 465c412b297da98b6e7a8926644ebf5ecf2faeaf
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:        An improved cmd.py for Writing Multi-command Scripts and Shells
Name:           python-cmdln
Version:        2.0.0
Release:        16%{?dist}
Source0:        https://github.com/trentm/cmdln/archive/%{commit}/cmdln-%{version}-%{shortcommit}.tar.gz
License:        MIT
BuildRequires:  python3-devel
URL:            https://github.com/trentm/cmdln
BuildArch:      noarch

%description
`cmdln.py` is an extension of Python's default `cmd.py` module that
provides "a simple framework for writing line-oriented command
interpreters".  The idea (with both cmd.py and cmdln.py) is to be able
to quickly build multi-sub-command tools (think cvs or svn) and/or
simple interactive shells (think gdb or pdb).  Cmdln's extensions make
it more natural to write sub-commands, integrate optparse for simple
option processing, and make having good command documentation easier.

%package doc
License:    MIT
Summary:    An improved cmd.py for Writing Multi-command Scripts and Shells

%description doc
`cmdln.py` is an extension of Python's default `cmd.py` module that
provides "a simple framework for writing line-oriented command
interpreters".  The idea (with both cmd.py and cmdln.py) is to be able
to quickly build multi-sub-command tools (think cvs or svn) and/or
simple interactive shells (think gdb or pdb).  Cmdln's extensions make
it more natural to write sub-commands, integrate optparse for simple
option processing, and make having good command documentation easier.

Documentation package.

%package -n python3-cmdln
License:    MIT
Summary:    An improved cmd.py for Writing Multi-command Scripts and Shells
%{?python_provide:%python_provide python3-cmdln}

%description -n python3-cmdln
`cmdln.py` is an extension of Python's default `cmd.py` module that
provides "a simple framework for writing line-oriented command
interpreters".  The idea (with both cmd.py and cmdln.py) is to be able
to quickly build multi-sub-command tools (think cvs or svn) and/or
simple interactive shells (think gdb or pdb).  Cmdln's extensions make
it more natural to write sub-commands, integrate optparse for simple
option processing, and make having good command documentation easier.

Python 3 compatible module.

%prep
%setup -q -n cmdln-%{version}

%build
export CFLAGS="%{optflags}"
%{__python3} setup.py build

%install
%{__python3} setup.py install \
   --prefix=%{_prefix} \
   --root=%{buildroot}

%files -n python3-cmdln
%license LICENSE.txt
%{python3_sitelib}/*

%files doc
%license LICENSE.txt
%doc README.md docs/* examples/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-14
- Subpackage python2-cmdln has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-8
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 20 2016 Andrea Veri <averi@fedoraproject.org> - 2.0.0-1
- New upstream release.
- Introduce a Python 3 package as upstream now supports it.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 08 2013 Andrea Veri <averi@fedoraproject.org> 1.3.0-2
- Remove [isa] from the -doc package requires, this is indeed a
  noarch package.

* Wed Dec 04 2013 Andrea Veri <averi@fedoraproject.org> 1.3.0-1
- First package release.
