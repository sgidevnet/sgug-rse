%global pkg undo-tree
%global pkgname "Undo Tree"

Name:		emacs-%{pkg}
Version:	0.6.4
Release:	8%{?dist}
Summary:	Treats undo history as a tree of changes

License:	GPLv3+
URL:		http://www.emacswiki.org/emacs/UndoTree
Source0:	http://www.dr-qubit.org/%{pkg}/%{pkg}.el

BuildArch:	noarch
BuildRequires:	emacs
Requires:	emacs(bin) >= %{_emacs_version}

%description
The undo-tree-mode provided by this package replaces Emacs' undo system with a
system that treats undo history as what it is: a branching tree of changes. This
simple idea allows the more intuitive behavior of the standard undo/redo system
to be combined with the power of never losing any history. An added side bonus
is that undo history can in some cases be stored more efficiently, allowing more
changes to accumulate before Emacs starts discarding history.

You don't have to imagine the undo tree, because undo-tree-mode includes an
undo-tree visualizer which draws it for you, and lets you browse around the undo
history.


%prep
cp -p %SOURCE0 .


%build
%{_emacs_bytecompile} %{pkg}.el


%install
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}
cp -p *.el *.elc $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}


%files
%{_emacs_sitelispdir}/%{pkg}



%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.6.4-1
- Update to version 0.6.4
- Update URLs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.5.3-2
- Fixed spelling

* Sat Aug 04 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.5.3-1
- Initial spec file

