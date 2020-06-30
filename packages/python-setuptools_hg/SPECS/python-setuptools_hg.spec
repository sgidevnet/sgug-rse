%global mod_name setuptools_hg

Name:           python-%{mod_name}
Version:        0.4
Release:        14%{?dist}
Summary:        Setuptools plugin for Mercurial version control

License:        GPLv2
URL:            http://pypi.python.org/pypi/%{mod_name}
Source0:        https://files.pythonhosted.org/packages/source/s/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
setuptools_hg is a plugin for setuptools that enables setuptools to find files
under the Mercurial version control system.It uses the Mercurial Python library
by default and falls back to use the command line program ``hg``. That's 
especially useful inside virtualenvs that don't have access to the system wide 
installed Mercurial lib (e.g. when created with ``--no-site-packages``).


%package -n python3-%{mod_name}
Summary:  %{summary}
%{?python_provide:%python_provide python3-%{mod_name}}

%description -n python3-%{mod_name}
setuptools_hg is a plugin for setuptools that enables setuptools to find files
under the Mercurial version control system.It uses the Mercurial Python library
by default and falls back to use the command line program ``hg``. That's 
especially useful inside virtualenvs that don't have access to the system wide 
installed Mercurial lib (e.g. when created with ``--no-site-packages``).
Python 3 version.


%prep
%setup -q -n %{mod_name}-%{version}

%build
%py3_build


%install
%py3_install


%files -n python3-%{mod_name}
%doc PKG-INFO
%license LICENSE
%{python3_sitelib}/%{mod_name}.*
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/__pycache__/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-9
- Subpackage python2-setuptools_hg has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4-2
- Rebuild for Python 3.6

* Thu Sep 01 2016 Dominika Krejci <dkrejci@redhat.com> - 0.4-1
- Update to 0.4
- Add Python3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2.1-2
- Add license file and some minor changes

* Wed Jul 13 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2.1-1
- Initial RPM release
