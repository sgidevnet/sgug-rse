%global modname unidiff


Name:           python-%{modname}
Version:        0.6.0
Release:        2%{?dist}
Summary:        Python library to parse and interact with unified diffs (patches)
License:        MIT
URL:            http://github.com/matiasb/python-unidiff
Source0:        https://files.pythonhosted.org/packages/source/u/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
Patch1:         0001-use-setuptools-console_scripts-for-usr-bin-unidiff.patch

%description
python-unidiff is a Python library to parse and interact with unified diffs 
(patches).

%package -n python%{python3_pkgversion}-%{modname}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{modname}
python-unidiff is a Python library to parse and interact with unified diffs 
(patches).

%prep
%setup -q -n %{modname}-%{version}
%patch1 -p1
rm -r unidiff.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m unittest discover -s tests/

%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE
%doc README.rst HISTORY
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Dan Callaghan <djc@djc.id.au> - 0.6.0-1
- new upstream release 0.6.0:
  https://github.com/matiasb/python-unidiff/blob/v0.6.0/HISTORY

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.5-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Dan Callaghan <dcallagh@redhat.com> - 0.5.5-2
- Fix requirements per new Python guidelines

* Tue Jan 09 2018 Dan Callaghan <dcallagh@redhat.com> - 0.5.5-1
- new upstream release 0.5.5:
  https://github.com/matiasb/python-unidiff/blob/v0.5.5/HISTORY

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Dan Callaghan <dcallagh@redhat.com> - 0.5.4-1
- new upstream release 0.5.4:
  https://github.com/matiasb/python-unidiff/blob/v0.5.4/HISTORY

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Dan Callaghan <dcallagh@redhat.com> - 0.5.2-2
- use %%license and %%python_provide, wrap %%description

* Fri Jun 17 2016 Dan Callaghan <dcallagh@redhat.com> - 0.5.2-1
- initial version
