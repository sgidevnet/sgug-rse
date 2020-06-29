# Review request: https://bugzilla.redhat.com/show_bug.cgi?id=1249313
%global srcname cmigemo
%global sum A pure python binding for C/Migemo
%global summ A C/Migemo binding for python written in pure python using ctypes.

Name:          python-%{srcname}
Version:       0.1.6
Release:       18%{?dist}
Summary:       %{sum}

License:       MIT
URL:           https://pypi.python.org/pypi/%{srcname}
Source0:       https://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: cmigemo-devel
BuildRequires: python3-six

%description
%{summ}

%package -n python3-%{srcname}
Summary:       %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summ}

%prep
%autosetup -n cmigemo-%{version}

# Remove upstream egg-info https://fedoraproject.org/wiki/Packaging:Python_Eggs#Upstream_Egg_Packages
rm -r %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.6-12
- Subpackage python2-cmigemo has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.6-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 17 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 0.1.6-2
- Review request https://bugzilla.redhat.com/show_bug.cgi?id=1249313 in progress, thank you to Julien Enselme.
- Make package to compatible with python 2 and 3 (https://fedoraproject.org/wiki/Packaging:Python#Example_common_spec_file), use new macroses.
- Rename spec and package without digit 3.
- Ask upstream about license file inclusion: https://github.com/mooz/python-cmigemo/issues/3

* Sat Aug 01 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 0.1.6-1
- My bug closed - version 0.1.6.

* Sun Jul 26 2015 Pavel Alexeev (aka Pahan-Hubbitus) <Pahan@Hubbitus.info> - 0.1.5-1
- Initial spec
- Test failed. Fill bugreport: https://github.com/mooz/python-cmigemo/issues/2
