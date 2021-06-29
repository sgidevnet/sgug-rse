Name:           python3-script
Version:        1.7.2
Release:        17%{?dist}
Summary:        Help for writing shell scripts in Python

License:        Python
URL:            http://lamb.cc/script/
Source0:        http://lamb.cc/script/script-%{version}.tar.gz
Source1:        LICENSE

BuildArch:      noarch
BuildRequires:  python3-devel
Provides:       python-script = %{version}-%{release}

%description
This module is mostly for folks who need to write a python script that will be
run from the command line. You know, something that can parse command line
arguments and run other external programs via the shell. The kind of script
you can call with --help. Something that perhaps reads, copies, deletes, or
otherwise manipulates files by their pathname.

If any of these apply, perhaps this module is for you!

A simple import script statement can provide your code with convenient command
line parsing, "a la carte" --help documentation, useful path operations, shell
command invocation with optional pipe redirection, and early run-time
termination with exit status control. Read on for more. Cheers!

%prep
%autosetup -n script-%{version}
install -m 0644 %{SOURCE1} .


%build
%py3_build


%install
%py3_install


%files
%doc README.txt
%license LICENSE
%{python3_sitelib}/script.py
%{python3_sitelib}/script-%{version}-*.egg-info
%{python3_sitelib}/__pycache__/script*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-14
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.7.2-7
- Provide python-script

* Thu Nov 19 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.7.2-6
- Use python macros

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.7.2-3
- Use license macro

* Thu Sep 18 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.7.2-2
- Add license file
- Update description

* Thu Aug 28 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.7.2-1
- First release of python3-script
