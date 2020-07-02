%global pkgname click-completion

Name:           python-click-completion
Version:        0.5.2
Release:        2%{?dist}
Summary:        Add automatic completion support for fish, Zsh, Bash and PowerShell to Click
License:        MIT
URL:            https://github.com/click-contrib/click-completion
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_enable_dependency_generator}

%description
Enhanced completion for Click

Add automatic completion support for fish, Zsh, Bash and PowerShell to Click.

All the supported shells are able to complete all the command line arguments
and options defined with click. In addition, fish and Zsh are also displaying
the options and commands help during the completion.


%package     -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}
%description -n python3-%{pkgname}
Enhanced completion for Click

Add automatic completion support for fish, Zsh, Bash and PowerShell to Click.

All the supported shells are able to complete all the command line arguments
and options defined with click. In addition, fish and Zsh are also displaying
the options and commands help during the completion.


%prep
%autosetup -n %{pkgname}-%{version}
sed -i 's|^#!/usr/bin/env python||' click_completion/__init__.py
sed -i 's|^#!/usr/bin/env python||' examples/click-completion-*
chmod -x examples/click-completion-*


%build
%{py3_build}


%install
%{py3_install}


%files -n python3-%{pkgname}
%license LICENSE
%doc examples README.md
%{python3_sitelib}/click_completion*/


%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.9

* Mon Feb 24 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.5.2
- Update to 0.5.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-1
- Update to 0.5.0
- Drop python2 subpackage

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.7

* Tue Apr  3 2018 Brett Lentz <brett.lentz@gmail.com> - 0.2.1-1
- initial package
