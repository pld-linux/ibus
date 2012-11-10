# TODO
# - clean .py in %{_datadir}/{setup,ui/gtk} if possible
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_without	vala		# Vala API
#
Summary:	Intelligent Input Bus for Linux OS
Summary(pl.UTF-8):	IBus - inteligentna szyna wejściowa dla Linuksa
Name:		ibus
Version:	1.4.99.20121006
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/ibus/downloads/list
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	28b26c84f021a0c15023d6326d4ad58e
Source1:	%{name}.xinputd
Patch0:		%{name}-HEAD.patch
Patch1:		%{name}-810211-no-switch-by-no-trigger.patch
Patch2:		%{name}-541492-xkb.patch
Patch3:		%{name}-530711-preload-sys.patch
Patch4:		%{name}-xx-setup-frequent-lang.patch
Patch5:		%{name}-xx-no-use.diff
URL:		http://code.google.com/p/ibus/
BuildRequires:	GConf2-devel >= 2.12
BuildRequires:	atk-devel
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.10
BuildRequires:	dconf-devel >= 0.7.5
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gobject-introspection-devel >= 0.6.8
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	libgnomekbd-devel
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	python-dbus-devel >= 0.83.0
BuildRequires:	python-pygobject-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.596
%{?with_vala:BuildRequires:	vala >= 2:0.14}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2 >= 2.12
Requires:	dbus >= 1.2.4
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	im-chooser
Requires:	iso-codes
Requires:	python-ibus = %{version}-%{release}
Requires:	python-pygtk-gtk
Requires:	python-pynotify
# input-keyboard-symbolic icon
Suggests:	gnome-icon-theme-symbolic
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus means Intelligent Input Bus. It is an input framework for Linux
OS.

%description -l pl.UTF-8
IBus (Intelligent Input Bus) to inteligentna szyna wejściowa. Jest to
szkielet wprowadzania tekstu dla Linuksa.

%package libs
Summary:	IBus library
Summary(pl.UTF-8):	Biblioteka IBus
Group:		Libraries
Requires:	glib2 >= 1:2.26.0

%description libs
This package contains the IBus shared library.

%description libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę współdzieloną IBus.

%package gtk2
Summary:	IBus im module for GTK+ 2.x
Summary(pl.UTF-8):	Moduł im IBus dla GTK+ 2.x
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	imsettings-gnome2
Requires(post):	glib2 >= 1:2.26.0

%description gtk2
This package contains IBus im module for GTK+ 2.x.

%description gtk2 -l pl.UTF-8
Ten pakiet zawiera moduł im IBus dla GTK+ 2.x.

%package gtk3
Summary:	IBus im module for GTK+ 3.x
Summary(pl.UTF-8):	Moduł im IBus dla GTK+ 3.x
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	imsettings-gnome3
Requires(post):	glib2 >= 1:2.26.0

%description gtk3
This package contains IBus im module for GTK+ 3.x.

%description gtk3 -l pl.UTF-8
Ten pakiet zawiera moduł im IBus dla GTK+ 3.x.

%package devel
Summary:	Development files for IBus
Summary(pl.UTF-8):	Pliki programistyczne IBus
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel

%description devel
The ibus-devel package contains the header files for IBus.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe dla szkieletu IBus.

%package static
Summary:	Static ibus library
Summary(pl.UTF-8):	Biblioteka statyczna ibus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ibus library.

%description static -l pl.UTF-8
Biblioteka statyczna ibus.

%package apidocs
Summary:	Development documentation for IBus
Summary(pl.UTF-8):	Dokumentacja programisty dla szkieletu IBus
Group:		Development/Libraries
Requires:	gtk-doc-common
Conflicts:	ibus-devel < 1.4.2

%description apidocs
Development documentation for IBus.

%description apidocs -l pl.UTF-8
Dokumentacja programisty dla szkieletu IBus.

%package -n python-ibus
Summary:	Python interface to IBus framework
Summary(pl.UTF-8):	Pythonowy interfejs do szkieletu IBus
Group:		Development/Languages/Python
Requires:	python-dbus >= 0.83.0
Requires:	python-pygobject
Requires:	python-pygtk-pango
Requires:	python-pyxdg
Conflicts:	ibus < 1.4.2

%description -n python-ibus
Python interface to IBus framework.

%description -n python-ibus -l pl.UTF-8
Pythonowy interfejs do szkieletu IBus.

%package -n vala-ibus
Summary:	Vala API for ibus library
Summary(pl.UTF-8):	API języka Vala do biblioteki ibus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.14

%description -n vala-ibus
Vala API for ibus library.

%description -n vala-ibus -l pl.UTF-8
API języka Vala do biblioteki ibus.

%package -n bash-completion-ibus
Summary:	Bash completion for ibus commands
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów dla poleceń ibus
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-ibus
Bash completion for ibus commands.

%description -n bash-completion-ibus -l pl.UTF-8
Bashowe dopełnianie parametrów dla poleceń ibus.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{__rm} bindings/vala/ibus-1.0.vapi
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk-doc \
	--disable-silent-rules \
	--enable-gconf \
	--enable-dconf \
	--enable-gtk2 \
	--enable-gtk3 \
	--enable-introspection \
	--enable-python-library \
	%{?with_static_libs:--enable-static} \
	--enable-surrounding-text \
	--enable-vala%{!?with_vala:=no} \
	--enable-xim \
	--enable-xkb \
	--enable-libgnomekbd \
	--with-html-dir=%{_gtkdocdir} \
	--with-no-snooper-apps='gnome-do,Do.*,firefox.*,.*chrome.*,.*chromium.*'

%{__make} -C ui/gtk3 maintainer-clean-generic

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{X11/xinit/xinput.d,xdg/autostart}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -e 's|@@LIB@@|%{_lib}|g' %{SOURCE1} >$RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d/ibus.conf

# correct location in upstream.
mv $RPM_BUILD_ROOT{%{_desktopdir},%{_sysconfdir}/xdg/autostart}/ibus.desktop

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk*/*/immodules/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk*/*/immodules/*.a
%endif

%py_postclean

%find_lang %{name}10

# imsettings will start this daemon for us
%{__rm} $RPM_BUILD_ROOT/etc/xdg/autostart/ibus.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install ibus.schemas
%glib_compile_schemas

%preun
%gconf_schema_uninstall ibus.schemas
%glib_compile_schemas

%postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%postun gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%post gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%postun gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%files -f %{name}10.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%config(noreplace) %verify(not md5 mtime size) /etc/X11/xinit/xinput.d/ibus.conf
%dir %{_sysconfdir}/dconf/db/ibus.d
%{_sysconfdir}/dconf/db/ibus.d/00-upstream-settings
%{_sysconfdir}/dconf/profile/ibus
%{_sysconfdir}/gconf/schemas/ibus.schemas
%attr(755,root,root) %{_bindir}/ibus
%attr(755,root,root) %{_bindir}/ibus-daemon
%attr(755,root,root) %{_bindir}/ibus-setup
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/ibus-dconf
%attr(755,root,root) %{_libexecdir}/ibus-engine-simple
%attr(755,root,root) %{_libexecdir}/ibus-gconf
%attr(755,root,root) %{_libexecdir}/ibus-ui-gtk3
%attr(755,root,root) %{_libexecdir}/ibus-x11
%attr(755,root,root) %{_libexecdir}/ibus-xkb
%{_datadir}/ibus
%{_datadir}/GConf/gsettings/ibus.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.gschema.xml
%{_desktopdir}/ibus-setup.desktop
%{_iconsdir}/hicolor/*/apps/ibus-*.png
%{_iconsdir}/hicolor/scalable/apps/ibus*.svg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibus-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibus-1.0.so.5
%{_libdir}/girepository-1.0/IBus-1.0.typelib

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/*/immodules/im-ibus.so

%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/*/immodules/im-ibus.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibus-1.0.so
%{_pkgconfigdir}/ibus-1.0.pc
%{_includedir}/ibus-1.0
%{_datadir}/gir-1.0/IBus-1.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libibus-1.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/ibus

%files -n python-ibus
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/ibus
%{py_sitescriptdir}/ibus/*.py[co]
%dir %{py_sitescriptdir}/ibus/interface
%{py_sitescriptdir}/ibus/interface/*.py[co]

%if %{with vala}
%files -n vala-ibus
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/ibus-1.0.vapi
%{_datadir}/vala/vapi/ibus-1.0.deps
%endif

%files -n bash-completion-ibus
%defattr(644,root,root,755)
/etc/bash_completion.d/ibus.bash
