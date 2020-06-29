%{?python_enable_dependency_generator}

%global modname orderedmultidict

Name:           python-%{modname}
Version:        1.0
Release:        9%{?dist}
Summary:        Ordered Multivalue Dictionary

License:        Unlicense
URL:            https://github.com/gruns/orderedmultidict
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{modname}; echo ${n:0:1})/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
A multivalue dictionary is a dictionary that can store multiple values for the
same key. An ordered multivalue dictionary is a multivalue dictionary that
retains the order of insertions and deletions.

%package -n python3-%{modname}
Summary:        Ordered Multivalue Dictionary
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

%description -n python3-%{modname}
A multivalue dictionary is a dictionary that can store multiple values for the
same key. An ordered multivalue dictionary is a multivalue dictionary that
retains the order of insertions and deletions.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
rm -vrf *.egg-info
chmod -x *.md
sed -i -e "s/'pycodestyle'//" setup.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{modname}
%license LICENSE.md
%doc API.md README.md
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-1
- Update to 1.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.11-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.11-2
- Rebuild for Python 3.6

* Sun Nov 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.11-1
- Update to 0.7.11

* Mon Oct 24 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.8-1
- Update to 0.7.8

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 05 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.7.6-1
- Update to 0.7.6

* Sun Apr 03 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.7.5-1
- Initial package
